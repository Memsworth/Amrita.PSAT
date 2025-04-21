# Geometric summation
from email.mime import image


def D1():
    TOTAL_SQUARES = 64
    GRAIN_WEIGHT_LBS = 1 / 7000

    totalGrain = 2**TOTAL_SQUARES - 1
    totalWeightInPounds = totalGrain * GRAIN_WEIGHT_LBS
    
    print("-" * 60)
    print(f"Total grains of wheat: {totalGrain:,}")
    print(f"Total weight in pounds: {totalWeightInPounds:,.2f} lbs")
    print("-" * 60)


def D2():

    def GetDataSizeInBits(amountOfData):
        EXA_BYTES = 10**18
        BYTES_TO_BITS = 8
        return (amountOfData * EXA_BYTES * BYTES_TO_BITS)
    
    def GetDownloadSpeedBitsPerSecond(downloadSpeed):
        MEGA_BITS_PER_SECOND = 10**6
        return (downloadSpeed * MEGA_BITS_PER_SECOND)

    def DisplayTotalTimeToDownload(size, speedInSeconds):
        seconds = size/speedInSeconds
        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24
        years = days / 365.25
        print("-" * 60)
        print(f"→ {seconds:,.0f} seconds")
        print(f"→ {minutes:,.0f} minutes")
        print(f"→ {hours:,.0f} hours")
        print(f"→ {days:,.0f} days")
        print(f"→ {years:,.2f} years")

    #Program starts here
    dataSpokenSoFar = 5
    userDownloadSpeed = int(input('What is your download speed: '))
    print(f"Downloading {dataSpokenSoFar} EB at {userDownloadSpeed} Mbps would take:")

    data = GetDataSizeInBits(dataSpokenSoFar)
    speed = GetDownloadSpeedBitsPerSecond(userDownloadSpeed)
    DisplayTotalTimeToDownload(data, speed)

def D3():
    def GetColorDepthSize(resolution_pixels, color_depth_bytes):
        return resolution_pixels * color_depth_bytes

    def GetSizeAfterCompression(original_size_bytes, compression_ratio):
        return original_size_bytes / compression_ratio

    def GetImageCount(color_depth_bits, compression_ratio, usb_size_gb):
        IMAGE_PIXELS = 800 * 600
        BYTES_PER_GB = 10**9
        color_depth_bytes = color_depth_bits / 8

        raw_size = GetColorDepthSize(IMAGE_PIXELS, color_depth_bytes)
        compressed_size = GetSizeAfterCompression(raw_size, compression_ratio)
        total_usb_bytes = usb_size_gb * BYTES_PER_GB

        image_count = total_usb_bytes // compressed_size
        return int(image_count)

    def GetGifSize(usb_size_gb):
        return GetImageCount(8, 5, usb_size_gb)

    def GetJpegSize(usb_size_gb):
        return GetImageCount(24, 25, usb_size_gb)

    def GetPngSize(usb_size_gb):
        return GetImageCount(24, 8, usb_size_gb)

    def GetTiffSize(usb_size_gb):
        return GetImageCount(48, 1, usb_size_gb)

    # Main execution
    usb_size = float(input("Enter USB size in GB: "))
    
    print(f"\nImages that can fit on a {usb_size} GB USB drive:")
    print("-" * 40)
    print(f"GIF  : {GetGifSize(usb_size):,} images")
    print(f"JPEG : {GetJpegSize(usb_size):,} images")
    print(f"PNG  : {GetPngSize(usb_size):,} images")
    print(f"TIFF : {GetTiffSize(usb_size):,} images")