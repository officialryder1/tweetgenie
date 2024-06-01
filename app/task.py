# from concurrent.futures import as_completed
# from django_thread import ThreadPoolExecutor


# def update_or_create_thing(name):
#     thing, _ = Thing.objects.update_or_create(name=name)
#     return thing.id


# executor = ThreadPoolExecutor()

# futures = []
# for i in range(5):
#     future = executor.submit(update_or_create_thing, f'Name i')
#     futures.append(future)

# ids = [f.result() for f in futures]

