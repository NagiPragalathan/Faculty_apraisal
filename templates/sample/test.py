from bing_image_downloader import downloader

a = downloader.download("css", limit=2, output_dir='new', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
print(a)