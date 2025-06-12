from flask import Blueprint, render_template, abort, current_app
from jinja2 import TemplateNotFound

# Blueprint for quest-related routes
quests_bp = Blueprint(
    "quests",
    __name__,
    template_folder="templates",
    url_prefix="/quests"
)

@quests_bp.route("/", methods=["GET"])
def list_quests():
    """
    Display the list of quests.
    Replace the 'quests_data' with actual data fetching logic as needed.
    """
    try:
        # Example placeholder for future database integration or service call
        quests_data = [
            {"id": 1, "title": "The Lost Sword", "description": "Find the ancient sword in the Ruins."},
            {"id": 2, "title": "Dragon's Lair", "description": "Defeat the dragon terrorizing the village."},
        ]
        return render_template("quests.html", quests=quests_data)
    except TemplateNotFound:
        current_app.logger.error("quests.html template not found")
        abort(404)

@quests_bp.route("/<int:quest_id>", methods=["GET"])
def quest_detail(quest_id):
    """
    Display details for a specific quest.
    Replace the example lookup with actual data fetching logic.
    """
    # Example placeholder data
    quest = next(
        (q for q in [
            {"id": 1, "title": "The Lost Sword", "description": "Find the ancient sword in the Ruins."},
            {"id": 2, "title": "Dragon's Lair", "description": "Defeat the dragon terrorizing the village."},
        ] if q["id"] == quest_id),
        None
    )
    if not quest:
        abort(404)
    return render_template("quest_detail.html", quest=quest)
