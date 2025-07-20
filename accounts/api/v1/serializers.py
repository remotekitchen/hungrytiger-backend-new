from accounts.api.base.serializers import BaseUserSerializer, BaseEmailPasswordLoginSerializer, BaseChangePasswordSerializer, BaseRestaurantUserSerializer, BaseUserAddressSerializer, BaseSalesRankingSerializer, BaseSalesUserWithInvitedSerializer, BaseSalesRankingSerializer


class UserSerializer(BaseUserSerializer):
    pass


class EmailPasswordLoginSerializer(BaseEmailPasswordLoginSerializer):
    pass


class ChangePasswordSerializer(BaseChangePasswordSerializer):
    pass


class RestaurantUserSerializer(BaseRestaurantUserSerializer):
    pass


class UserAddressSerializer(BaseUserAddressSerializer):
    pass


class SalesRankingSerializer(BaseSalesRankingSerializer):
    pass
class InvitedUserSerializer(BaseSalesUserWithInvitedSerializer):
    pass

class SalesUserRankingView(BaseSalesRankingSerializer):
    pass
