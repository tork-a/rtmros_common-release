Name:           ros-hydro-rtmbuild
Version:        1.2.5
Release:        0%{?dist}
Summary:        ROS rtmbuild package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rtmbuild
Source0:        %{name}-%{version}.tar.gz

Requires:       blas-devel
Requires:       lapack-devel
Requires:       omniORB
Requires:       omniORB-devel
Requires:       omniORB-servers
Requires:       pkgconfig
Requires:       ros-hydro-cmake-modules
Requires:       ros-hydro-message-generation
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-openrtm-aist
Requires:       ros-hydro-openrtm-aist-python
Requires:       ros-hydro-rostest
Requires:       ros-hydro-std-msgs
BuildRequires:  omniORB
BuildRequires:  omniORB-devel
BuildRequires:  omniORB-servers
BuildRequires:  pkgconfig
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-openrtm-aist
BuildRequires:  ros-hydro-openrtm-aist-python
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-std-msgs

%description
Build scripts for OpenRTM and OpenHRP

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
* Sat Oct 04 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.5-0
- Autogenerated by Bloom

* Mon Sep 08 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.4-1
- Autogenerated by Bloom

* Mon Sep 08 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.4-0
- Autogenerated by Bloom

* Wed Sep 03 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.3-0
- Autogenerated by Bloom

* Sun Aug 31 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.2-0
- Autogenerated by Bloom

