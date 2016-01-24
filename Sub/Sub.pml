<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Sub" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="__init__" src="lib/paho/__init__.py" />
        <File name="__init__" src="lib/paho/mqtt/__init__.py" />
        <File name="client" src="lib/paho/mqtt/client.py" />
        <File name="publish" src="lib/paho/mqtt/publish.py" />
    </Resources>
    <Topics />
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
</Package>
