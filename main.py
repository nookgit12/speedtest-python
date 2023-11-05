import speedtest

st = speedtest.Speedtest()
download_speed = st.download() / 1024 / 1024  # Convert to Mbps
upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

print(f"Download Speed: {download_speed:.2f} Mbps")
print(f"Upload Speed: {upload_speed:.2f} Mbps")