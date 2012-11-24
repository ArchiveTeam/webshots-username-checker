#!/usr/bin/env python

from seesaw.externalprocess import *
from seesaw.pipeline import *
from seesaw.project import *

pipeline = Pipeline(
    ExternalProcess("WebshotsDiscovery", ["./discover-webshots.py"])
    ExternalProcess("WebshotsChecker", ["./check-webshots.py"])
)

project = Project(
    title = "Webshots checker",
    project_html = """
    <h2>Webshots checker</h2>
    <p>Help to discover valid Webshots usernames.</p>
    """
)
