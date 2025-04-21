# Geometric Summation (Grains of Wheat Problem)
def D1():
    # Constants for the problem
    TOTAL_SQUARES = 64
    GRAIN_WEIGHT_LBS = 1 / 7000  # Weight of one grain of wheat in pounds

    # Calculate total grains of wheat and total weight
    totalGrain = 2**TOTAL_SQUARES - 1
    totalWeightInPounds = totalGrain * GRAIN_WEIGHT_LBS
    
    # Display the results
    print("-" * 60)
    print(f"Total grains of wheat: {totalGrain:,}")
    print(f"Total weight in pounds: {totalWeightInPounds:,.2f} lbs")
    print("-" * 60)
############## Geometric Summation End ##############



# File Download Time Calculation
def D2():

    # Function to calculate data size in bits (Exabytes to bits)
    def GetDataSizeInBits(amountOfData):
        EXA_BYTES = 10**18
        BYTES_TO_BITS = 8
        return (amountOfData * EXA_BYTES * BYTES_TO_BITS)
    
    # Function to calculate download speed in bits per second
    def GetDownloadSpeedBitsPerSecond(downloadSpeed):
        MEGA_BITS_PER_SECOND = 10**6
        return (downloadSpeed * MEGA_BITS_PER_SECOND)

    # Function to display total download time in different units
    def DisplayTotalTimeToDownload(size, speedInSeconds):
        seconds = size / speedInSeconds
        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24
        years = days / 365.25
        
        # Print the results in different units
        print("-" * 60)
        print(f"→ {seconds:,.0f} seconds")
        print(f"→ {minutes:,.0f} minutes")
        print(f"→ {hours:,.0f} hours")
        print(f"→ {days:,.0f} days")
        print(f"→ {years:,.2f} years")

    # Main execution of D2
    dataSpokenSoFar = 5  # Amount of data in Exabytes (EB)
    userDownloadSpeed = int(input('What is your download speed (in Mbps)? '))
    
    print(f"\nDownloading {dataSpokenSoFar} EB at {userDownloadSpeed} Mbps would take:")
    
    # Calculate download time
    data = GetDataSizeInBits(dataSpokenSoFar)
    speed = GetDownloadSpeedBitsPerSecond(userDownloadSpeed)
    DisplayTotalTimeToDownload(data, speed)
############## File Download Time End ##############



# Image Storage Calculation (USB size and image formats)
def D3():
    
    # Function to calculate the size of an image based on resolution and color depth
    def GetColorDepthSize(resolution_pixels, color_depth_bytes):
        return resolution_pixels * color_depth_bytes

    # Function to calculate size after compression
    def GetSizeAfterCompression(original_size_bytes, compression_ratio):
        return original_size_bytes / compression_ratio

    # Function to calculate the number of images that can fit in a USB drive
    def GetImageCount(color_depth_bits, compression_ratio, usb_size_gb):
        IMAGE_PIXELS = 800 * 600  # Resolution of the image (800x600)
        BYTES_PER_GB = 10**9  # Bytes per GB
        
        color_depth_bytes = color_depth_bits / 8  # Convert color depth from bits to bytes
        raw_size = GetColorDepthSize(IMAGE_PIXELS, color_depth_bytes)
        compressed_size = GetSizeAfterCompression(raw_size, compression_ratio)
        total_usb_bytes = usb_size_gb * BYTES_PER_GB

        # Calculate how many images fit in the given USB size
        image_count = total_usb_bytes // compressed_size
        return int(image_count)

    # Functions to calculate the number of images based on format
    def GetGifSize(usb_size_gb):
        return GetImageCount(8, 5, usb_size_gb)

    def GetJpegSize(usb_size_gb):
        return GetImageCount(24, 25, usb_size_gb)

    def GetPngSize(usb_size_gb):
        return GetImageCount(24, 8, usb_size_gb)

    def GetTiffSize(usb_size_gb):
        return GetImageCount(48, 1, usb_size_gb)

    # Main execution of D3
    usb_size = float(input("Enter USB size in GB: "))
    
    print(f"\nImages that can fit on a {usb_size} GB USB drive:")
    print("-" * 40)
    print(f"GIF  : {GetGifSize(usb_size):,} images")
    print(f"JPEG : {GetJpegSize(usb_size):,} images")
    print(f"PNG  : {GetPngSize(usb_size):,} images")
    print(f"TIFF : {GetTiffSize(usb_size):,} images")
############## Image Storage Calculation End ##############



# Heartbeats and Breaths over a Lifetime (Health Metrics)
def D4():
    
    # Function to calculate age in seconds
    def GetAgeInSeconds(user_age):
        seconds_per_year = 365.25 * 24 * 60 * 60  # Seconds in a year
        return int(user_age * seconds_per_year)
    
    # Function to calculate total heartbeats over a lifetime
    def GetHeartBeatsPerSecond(user_age):
        heart_rate = float(67.5)  # Average heart rate in beats per minute
        return round((heart_rate * GetAgeInSeconds(user_age)), 2)
    
    # Function to calculate total breaths over a lifetime
    def GetBreathPerMin(user_age):
        # Breathing rates per age group (average breaths per minute)
        infant = (30 + 60) // 2
        one_to_four = (20 + 30) // 2
        five_to_fourteen = (15 + 25) // 2
        adult = (12 + 20) // 2
        
        minutes_in_year = 365.25 * 24 * 60  # Minutes in a year
        total_breath = 0
        
        # Loop through each year and calculate total breaths
        for year in range(user_age):
            if year < 1:
                bpm = infant
            elif 1 <= year <= 4:
                bpm = one_to_four
            elif 5 <= year <= 14:
                bpm = five_to_fourteen
            else:
                bpm = adult
            total_breath += int(bpm * minutes_in_year)
        return total_breath

    # Main execution of D4
    user_age = int(input('Enter your age: '))
    
    # Calculate total heartbeats and breaths
    total_heart_rate = GetHeartBeatsPerSecond(user_age)
    total_breath_rate = GetBreathPerMin(user_age)

    # Display the results
    print(f"Estimated heartbeats in your life: {total_heart_rate:,}")
    print(f"Estimated breaths in your life: {total_breath_rate:,}")
############## Heartbeats and Breaths Calculation End ##############