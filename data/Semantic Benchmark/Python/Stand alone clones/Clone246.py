def changelist_view(self, request, extra_context = None) :
	default_filter = False
	try :
		ref = request.META ['HTTP_REFERER']
		pinfo = request.META ['PATH_INFO']
		qstr = ref.split(pinfo)
		querystr = request.META ['QUERY_STRING']
		if querystr is None :
			if len(qstr) < 2 or qstr [1] == '' :
				default_filter = True
	except :
		default_filter = True
	if default_filter :
		q = request.GET.copy()
		q ['registered__isnull'] = 'True'
		request.GET = q
		request.META ['QUERY_STRING'] = request.GET.urlencode()
	return super(MyAdmin, self).changelist_view(request, extra_context = extra_context)


def changelist_view(self, request, extra_context = None) :
	test = request.META ['HTTP_REFERER'].split(request.META ['PATH_INFO'])
	if test [- 1] and not test [- 1].startswith('?') :
		if not request.GET.has_key('decommissioned__exact') :
			q = request.GET.copy()
			q ['decommissioned__exact'] = 'N'
			request.GET = q
			request.META ['QUERY_STRING'] = request.GET.urlencode()
	return super(MyModelAdmin, self).changelist_view(request, extra_context = extra_context)

