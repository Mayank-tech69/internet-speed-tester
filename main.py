import speedtest
test=speedtest.Speedtest()
test.get_servers()
test.get_best_server()
download=test.download()/(1024 * 1024)
upload=test.upload()/(1024 * 1024)
print(f"download speed is:  {download:.2f} Mbps")
print(f"upload speed is:  {upload:.2f} Mbps")