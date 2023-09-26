days_in_month = {'Jan':31, 'Feb':28, 'Mar':31}
days_in_month2 = {'Apr':30, 'May':31, 'Jun':30}
days_in_month.update({'Nov':21, 'Dec':30})
del days_in_month['Dec']
print(days_in_month.items())
print(days_in_month.get('January'))