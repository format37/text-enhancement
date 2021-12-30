import asyncio
from aiohttp import web
import os
import json
import torch
from datetime import datetime

# Model init
model, example_texts, languages, punct, apply_te = torch.hub.load(
	repo_or_dir='snakers4/silero-models',
	model='silero_te'
	)
print(datetime.now(), 'ready')


async def call_test(request):	
	content = "ok"	
	return web.Response(text=content, content_type="text/html")


async def call_te(request):	
	request_str = json.loads(str(await request.text()))
	request = json.loads(request_str)
	print(datetime.now(), request['lan'], 'request:', len(request['in_text']))	
	response = apply_te(request['in_text'], lan=request['lan'])
	print(datetime.now(), 'response:', response)
	return web.Response(text=str(response), content_type="text/html")


app = web.Application(client_max_size=1024**3)
app.router.add_route('GET', '/test', call_test)
app.router.add_post('/te', call_te)

web.run_app(
	app,
	port=os.environ.get('PORT', ''),
)
