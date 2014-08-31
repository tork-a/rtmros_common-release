Name:           ros-hydro-hrpsys-ros-bridge
Version:        1.2.2
Release:        0%{?dist}
Summary:        ROS hrpsys_ros_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/hrpsys_ros_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       python-ipython
Requires:       python-psutil
Requires:       ros-hydro-actionlib
Requires:       ros-hydro-camera-info-manager
Requires:       ros-hydro-collada-urdf
Requires:       ros-hydro-control-msgs
Requires:       ros-hydro-diagnostic-aggregator
Requires:       ros-hydro-diagnostic-msgs
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-hrpsys
Requires:       ros-hydro-hrpsys-tools
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-pr2-controllers
Requires:       ros-hydro-robot-state-publisher
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rosnode
Requires:       ros-hydro-rostest
Requires:       ros-hydro-rqt-gui
Requires:       ros-hydro-rqt-gui-py
Requires:       ros-hydro-rqt-robot-dashboard
Requires:       ros-hydro-rqt-robot-monitor
Requires:       ros-hydro-rtmbuild
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-tf
Requires:       ros-hydro-visualization-msgs
BuildRequires:  git
BuildRequires:  hostname
BuildRequires:  net-tools
BuildRequires:  pkgconfig
BuildRequires:  procps-ng
BuildRequires:  python-rosdep
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-angles
BuildRequires:  ros-hydro-camera-info-manager
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-collada-urdf
BuildRequires:  ros-hydro-control-msgs
BuildRequires:  ros-hydro-diagnostic-aggregator
BuildRequires:  ros-hydro-diagnostic-msgs
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-hrpsys >= 315.2.0
BuildRequires:  ros-hydro-hrpsys-tools
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-pr2-controllers
BuildRequires:  ros-hydro-robot-state-publisher
BuildRequires:  ros-hydro-rosbuild
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-roslang
BuildRequires:  ros-hydro-rosnode
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-rqt-gui
BuildRequires:  ros-hydro-rqt-gui-py
BuildRequires:  ros-hydro-rqt-robot-dashboard
BuildRequires:  ros-hydro-rqt-robot-monitor
BuildRequires:  ros-hydro-rtmbuild
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-visualization-msgs
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
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sun Aug 31 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.2-0
- Autogenerated by Bloom

