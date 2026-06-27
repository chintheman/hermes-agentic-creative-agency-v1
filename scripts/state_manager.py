#!/usr/bin/env python3
"""Agency State Manager — Initialize and manage project state files."""
import json, os, uuid, sys
from datetime import datetime

WORKSPACE = os.path.expanduser("~/agency_workspace")
SCHEMA_PATH = os.path.join(WORKSPACE, "schemas", "state-schema.json")

def init_project(name, brand, brief, fmt, audience="", deadline=""):
    """Create a new project with initial state."""
    project_id = str(uuid.uuid4())[:8]
    project_dir = os.path.join(WORKSPACE, "projects", project_id)
    os.makedirs(project_dir, exist_ok=True)
    
    now = datetime.utcnow().isoformat() + "Z"
    
    state = {
        "project": {
            "id": project_id,
            "name": name,
            "brand": brand,
            "brief": brief,
            "format": fmt,
            "audience": audience,
            "deadline": deadline,
            "status": "ideation",
            "current_stage": -1,
            "created_at": now,
            "updated_at": now
        },
        "state": {
            "pipeline_progress": {
                "stage_-1_complete": False,
                "stage_0_complete": False,
                "stage_1_complete": False,
                "stage_2_complete": False,
                "stage_3_complete": False,
                "stage_4_complete": False,
                "stage_5_complete": False
            },
            "current_sub_stage": None,
            "stage_2_output": {
                "copy_block": "",
                "humanizer_applied": False,
                "brand_voice_verified": False
            },
            "stage_3_output": {
                "visual_paths": [],
                "low_res_draft": False,
                "final_rendered": False
            },
            "stage_4_output": {
                "image_critique_score": 0,
                "design_lint_verdict": "pending",
                "brand_check_score": 0,
                "critic_scores": {},
                "gate_verdict": "pending",
                "review_notes": []
            }
        },
        "artifacts": {
            "generated_files": [],
            "current_version": 0
        },
        "feedback": {
            "human_interventions": [],
            "structured_feedback": {
                "likes": [],
                "changes": [],
                "direction_changes": []
            }
        },
        "cost_tracking": {
            "api_calls": 0,
            "estimated_cost_usd": 0.0,
            "model_breakdown": {
                "deepseek_v4_pro": 0,
                "deepseek_v4_flash": 0,
                "claude_sonnet_4_6": 0,
                "image_generations": 0,
                "video_generations": 0
            }
        }
    }
    
    path = os.path.join(project_dir, "state.json")
    with open(path, "w") as f:
        json.dump(state, f, indent=2)
    
    print(f"✅ Project '{name}' created (ID: {project_id})")
    print(f"   State: {path}")
    return project_id

def get_state(project_id):
    """Load project state."""
    path = os.path.join(WORKSPACE, "projects", project_id, "state.json")
    if not os.path.exists(path):
        print(f"❌ Project {project_id} not found")
        return None
    with open(path) as f:
        return json.load(f)

def update_state(project_id, updates):
    """Update project state with partial dict."""
    state = get_state(project_id)
    if not state:
        return False
    _deep_merge(state, updates)
    state["project"]["updated_at"] = datetime.utcnow().isoformat() + "Z"
    path = os.path.join(WORKSPACE, "projects", project_id, "state.json")
    with open(path, "w") as f:
        json.dump(state, f, indent=2)
    print(f"✅ Project {project_id} state updated")
    return True

def _deep_merge(base, updates):
    """Recursively merge updates into base dict."""
    for key, val in updates.items():
        if isinstance(val, dict) and key in base and isinstance(base[key], dict):
            _deep_merge(base[key], val)
        else:
            base[key] = val

def list_projects():
    """List all active projects."""
    projects_dir = os.path.join(WORKSPACE, "projects")
    if not os.path.exists(projects_dir):
        return []
    projects = []
    for pid in os.listdir(projects_dir):
        state_path = os.path.join(projects_dir, pid, "state.json")
        if os.path.exists(state_path):
            with open(state_path) as f:
                s = json.load(f)
            projects.append({
                "id": pid,
                "name": s["project"]["name"],
                "brand": s["project"]["brand"],
                "status": s["project"]["status"],
                "stage": s["project"]["current_stage"]
            })
    return projects

def add_feedback(project_id, likes=None, changes=None, direction_changes=None):
    """Add structured feedback to a project."""
    state = get_state(project_id)
    if not state:
        return False
    fb = state["feedback"]["structured_feedback"]
    if likes: fb["likes"].extend(likes)
    if changes: fb["changes"].extend(changes)
    if direction_changes: fb["direction_changes"].extend(direction_changes)
    
    # Also write to workspace feedback dir
    feedback_path = os.path.join(WORKSPACE, "feedback", f"{project_id}.json")
    with open(feedback_path, "w") as f:
        json.dump({
            "project_id": project_id,
            "brand": state["project"]["brand"],
            "likes": fb["likes"],
            "changes": fb["changes"],
            "direction_changes": fb["direction_changes"],
            "applied_to": []
        }, f, indent=2)
    
    update_state(project_id, {"feedback": state["feedback"]})
    print(f"✅ Feedback saved for project {project_id}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 state_manager.py <command> [args]")
        print("Commands: init <name> <brand> <brief> <format>")
        print("          list")
        print("          feedback <project_id> --likes '...' --changes '...'")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "init" and len(sys.argv) >= 5:
        init_project(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif cmd == "list":
        for p in list_projects():
            print(f"  [{p['id']}] {p['name']} — {p['brand']} — {p['status']} (Stage {p['stage']})")
    elif cmd == "feedback" and len(sys.argv) >= 3:
        add_feedback(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")
