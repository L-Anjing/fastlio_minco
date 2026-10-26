#!/usr/bin/env bash
set -euo pipefail

WORKSPACE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROS_SETUP="/opt/ros/humble/setup.bash"

if [[ ! -f "${ROS_SETUP}" ]]; then
  echo "ROS 2 Humble setup not found: ${ROS_SETUP}" >&2
  exit 1
fi

source "${ROS_SETUP}"
cd "${WORKSPACE_DIR}"

echo "Building workspace in Release mode..."
colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release

echo
echo "Build complete. In each new terminal, run:"
echo "  source /opt/ros/humble/setup.bash"
echo "  source ${WORKSPACE_DIR}/install/setup.bash"
