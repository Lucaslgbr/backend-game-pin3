from backend.game.api.v1.viewsets.match_viewset import MatchViewset
from backend.game.api.v1.viewsets.room_viewset import RoomViewset
from backend.game.api.v1.viewsets.user_viewset import UserViewset

viewsets = [
    {'path':'user','viewset':UserViewset},
    {'path':'room','viewset':RoomViewset},
    {'path':'match','viewset':MatchViewset},
]