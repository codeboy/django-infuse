django-infuse
=============

Series of Class based mixins.  Requires Django 1.4s use of PermissionDenied exception. 

Installation
------------

    pip install django-infuse
    
Currently Supported Mixins
--------------------------

* Permission Required
* Staff Required
* Super User required
* Login Required
* Group Required

Usage
-----

Inherit the mixin you want to use and add any additional (optional) params.

	from infuse.auth.permissions import LoginRequiredMixin

	class MyLoginProtectedView(LoginRequiredMixin, ListView):
		# If login_url is not the url you want to redirect
		# users to, set one here.

		login_url = "/my/new/url/"

		# Do the rest of your stuff.....

The only other different one is GroupRequiredMixin

	from infuse.auth.permissions import GroupRequiredMixin

	class MyGroupRequiredView(GroupRequiredMixin, ListView):
		# Uses login_required, so you can optionally pass in
		# a url just like LoginRequired.

		# You MUST set a group, Infuse will throw an exception
		# if you do not.

		group = "My Awesome Group"