#!/bin/bash
echo "=== system_profiler: hardware ==="
system_profiler SPHardwareDataType | grep -E "Model Name|Chip:|Total Number of Cores|Memory:"
echo
echo "=== system_profiler: GPU ==="
system_profiler SPDisplaysDataType | grep -E "Chipset Model|Total Number of Cores|Metal Support"
echo
echo "=== torch framework query ==="
python -c "import torch; print('torch version:', torch.__version__); print('cuda available:', torch.cuda.is_available()); print('mps available:', torch.backends.mps.is_available())"
