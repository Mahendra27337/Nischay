from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from .models import Notification, UserProfile
@csrf_exempt
def bot_register(request):
    if request.method!='POST': return JsonResponse({'error':'use POST'}, status=400)
    data = json.loads(request.body)
    username = data.get('username'); password = data.get('password'); kyc = data.get('kyc_id')
    if not username or not password:
        return JsonResponse({'error':'username and password required'}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error':'username exists'}, status=400)
    if kyc and UserProfile.objects.filter(kyc_id=kyc).exists():
        return JsonResponse({'error':'duplicate kyc'}, status=400)
    user = User.objects.create_user(username=username, password=password)
    UserProfile.objects.create(user=user, kyc_id=kyc)
    Notification.objects.create(user=user, event_type='REG', message=f'New user {username} via bot')
    return JsonResponse({'message':'registered'}, status=201)
@csrf_exempt
def request_withdrawal(request):
    if request.method!='POST': return JsonResponse({'error':'use POST'}, status=400)
    data = json.loads(request.body); user_id = data.get('user_id'); amount = float(data.get('amount',0))
    try:
        profile = UserProfile.objects.get(user_id=user_id)
    except UserProfile.DoesNotExist:
        return JsonResponse({'error':'user not found'}, status=404)
    if profile.wallet_balance < amount: return JsonResponse({'error':'insufficient balance'}, status=400)
    profile.wallet_balance -= amount; profile.save()
    Notification.objects.create(user=profile.user, event_type='WD', message=f'Auto withdrawal of {amount} for {profile.user.username}')
    return JsonResponse({'message':'withdrawal processed'})
def check_franchise(request, user_id):
    try:
        profile = UserProfile.objects.get(user_id=user_id)
    except UserProfile.DoesNotExist:
        return JsonResponse({'error':'user not found'}, status=404)
    return JsonResponse({'eligible': profile.referral_count>=2000, 'count': profile.referral_count})
