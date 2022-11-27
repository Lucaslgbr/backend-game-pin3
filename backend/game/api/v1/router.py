from backend.game.api.v1.viewsets import *

viewsets = [
    {'path':'user','viewset':UserViewset},
    {'path':'room','viewset':RoomViewset},
    {'path':'match','viewset':MatchViewset},
    {'path':'match_user','viewset':MatchUserViewset},
    {'path':'board','viewset':BoardViewset},
    
]