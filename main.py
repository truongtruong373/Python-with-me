import torch

# Kiểm tra xem CUDA có khả dụng không
if torch.cuda.is_available():
    # Lấy số lượng GPU
    num_devices = torch.cuda.device_count()
    print(f"Số lượng GPU khả dụng: {num_devices}")
    
    # Lấy tên của từng GPU
    for i in range(num_devices):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("CUDA không khả dụng.")
print("my name is truong")
