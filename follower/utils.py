from authentication.models import User
from .models import Follower

class FollowRequestAcceptDeny():

    action= ['Accept', 'Deny']

    def accept_request(self,user_to_follow):
        if self.action=="Accept":
            self.followed_by.add(user_to_follow)
            self.save()

    def deny_request(self,user_to_follow):
        if self.action== "Deny":
            self.requested_by.remove(user_to_follow)
            self.save()

