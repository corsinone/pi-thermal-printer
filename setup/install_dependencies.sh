echo "*** Updating system packages..."
apt update && apt upgrade -y
echo "*** Done."
echo "*** Installing required system packages..."
apt install -y git python3 python3-serial
echo "*** Done."
