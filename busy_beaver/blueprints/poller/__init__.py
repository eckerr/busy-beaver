from flask import blueprints

from .github_summary import PublishGitHubSummaryResource
from .retweeter import TwitterPollingResource
from .upcoming_events import PublishUpcomingEventsResource
from .update_events import AddEventPollingResource
from .youtube_post import YouTubePollingResource
from busy_beaver.blueprints.toolbox import authentication_required

poller_bp = blueprints.Blueprint("poller", __name__)
admin_role_required = authentication_required(roles=["admin"])

view = PublishGitHubSummaryResource.as_view("post_github_summary")
poller_bp.add_url_rule(
    "/github-summary", view_func=admin_role_required(view), methods=["POST"]
)

view = TwitterPollingResource.as_view("twitter_poller")
poller_bp.add_url_rule(
    "/twitter", view_func=admin_role_required(view), methods=["POST"]
)

view = PublishUpcomingEventsResource.as_view("post_upcoming_events")
poller_bp.add_url_rule(
    "/upcoming-events", view_func=admin_role_required(view), methods=["POST"]
)

view = AddEventPollingResource.as_view("meetup_poller")
poller_bp.add_url_rule(
    "/sync-event-database", view_func=admin_role_required(view), methods=["POST"]
)

view = YouTubePollingResource.as_view("youtube_poller")
poller_bp.add_url_rule(
    "/youtube", view_func=admin_role_required(view), methods=["POST"]
)
