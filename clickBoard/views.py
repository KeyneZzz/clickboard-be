from rest_framework.views import APIView
from rest_framework.response import Response

import traceback
import json

class clickBoard(APIView):
	def get(self,request):
		try:
			f = open('clipboardObjects.json','r',encoding='utf-8')
			data=json.loads(f.read())
			f.close()
			return Response(data,200)
		except FileNotFoundError:
			f = open('clipboardObjects.json','w',encoding='utf-8')
			f.write('[]')
			f.close()
			return Response([],200)
		except Exception as e:
			traceback.print_exc()
			return Response(None,500)
	def put(self,request):
		try:
			f = open('clipboardObjects.json','w',encoding='utf-8')
			f.write(request.body.decode())
			f.close()
			return Response(None,200)
		except Exception as e:
			traceback.print_exc()
			return Response(None,500)
	

