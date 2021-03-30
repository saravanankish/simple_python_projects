import speedtest

st = speedtest.Speedtest()
print("Checking Download speed...")
print("Your download speed is", st.download() // 10 ** 6, "Mbps")
print("Checking Upload speed...")
print("Your upload speed is", st.upload() // 10 ** 6, "Mbps")
print("Checking Ping...")
print("Your ping is", int(st.results.ping), "MS")
