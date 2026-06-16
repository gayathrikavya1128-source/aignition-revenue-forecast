
set -e

py -3.13 src/generate_features.py
py -3.13 src/predict.py

echo "Done!"