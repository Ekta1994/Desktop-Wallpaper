# Desktop-Wallpaper
This utility lets you change your desktop's wallpaper randomly whenever any user logs in.

#Required
	-Python should be installed (>=2.7)

1) Place the above folder "wallpaper" and the python script whenever you want to put in your system.
2) The python script reads the "wallpaper" directory and choses one to put on desktop randomly. 
3.) We now need to specify that this script should run automatically when a user logs in. This can be achieved in many ways :-
	- Explicitly by modifying in task scheduler
	- By creating a batch script
	
#Create a task in task scheduler
1.) Go to Start menu and then click on Administrative tools
2.) From the options which come in, select Task scheduler.
3.) A window will open up, there'll be an option "Create Task" in the right panel.
4.) Create Task window will then open up.
	- In "General" tab, mention any name for your task
	- In "Triggers" tab, click on new and then specify when it should be triggered. Select "workstation unlock" in the dropdown.
	- In "Actions" tab, there'll be a settings option. Mention the path to your python.exe (eg, C:\Python27\python.exe ) and add the path to your python script (wallpaper.py) in the arguments.
	- In "Conditions" tab, uncheck the power button
That's all, you have created one task for windows to run when any user logs in to your system. This task will run the python script whose path you have mentioned while creating the task.
