Name:           ros-kinetic-hrpsys-ros-bridge
Version:        1.4.0
Release:        0%{?dist}
Summary:        ROS hrpsys_ros_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/hrpsys_ros_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       python-ipython
Requires:       python-psutil
Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-camera-info-manager
Requires:       ros-kinetic-collada-urdf
Requires:       ros-kinetic-control-msgs
Requires:       ros-kinetic-diagnostic-aggregator
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-hrpsys
Requires:       ros-kinetic-hrpsys-tools
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-pr2-msgs
Requires:       ros-kinetic-robot-pose-ekf
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rosnode
Requires:       ros-kinetic-rostest
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-py
Requires:       ros-kinetic-rqt-robot-dashboard
Requires:       ros-kinetic-rqt-robot-monitor
Requires:       ros-kinetic-rtmbuild
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  git
BuildRequires:  hostname
BuildRequires:  net-tools
BuildRequires:  pkgconfig
BuildRequires:  procps-ng
BuildRequires:  python-rosdep
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-angles
BuildRequires:  ros-kinetic-camera-info-manager
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-collada-urdf
BuildRequires:  ros-kinetic-control-msgs
BuildRequires:  ros-kinetic-diagnostic-aggregator
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-euscollada
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-hrpsys >= 315.3.1
BuildRequires:  ros-kinetic-hrpsys-tools
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-mk
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-pr2-msgs
BuildRequires:  ros-kinetic-robot-pose-ekf
BuildRequires:  ros-kinetic-robot-state-publisher
BuildRequires:  ros-kinetic-rosbuild
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslang
BuildRequires:  ros-kinetic-rosnode
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rqt-gui
BuildRequires:  ros-kinetic-rqt-gui-py
BuildRequires:  ros-kinetic-rqt-robot-dashboard
BuildRequires:  ros-kinetic-rqt-robot-monitor
BuildRequires:  ros-kinetic-rtmbuild
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  subversion

%description
hrpsys_ros_bridge package provides basic functionalities to bind hrpsys, a
OpenRTM-based controller, and ROS. By using this package, you can write your ROS
packages that communicate with your non-ROS robots that run on hrpsys. For
communicating with the robots that run on OpenRTM without hrpsys, you can use
openrtm_ros_bridge package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Aug 09 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.4.0-0
- Autogenerated by Bloom

