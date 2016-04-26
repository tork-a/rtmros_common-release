Name:           ros-indigo-rtmbuild
Version:        1.3.2
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
Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-openrtm-aist
Requires:       ros-indigo-openrtm-aist-python
Requires:       ros-indigo-rostest
Requires:       ros-indigo-std-msgs
BuildRequires:  omniORB
BuildRequires:  omniORB-devel
BuildRequires:  omniORB-servers
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-openrtm-aist
BuildRequires:  ros-indigo-openrtm-aist-python
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-msgs

%description
Build scripts for OpenRTM and OpenHRP

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Apr 26 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.2-0
- Autogenerated by Bloom

* Thu Dec 17 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.1-0
- Autogenerated by Bloom

* Wed Dec 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.0-0
- Autogenerated by Bloom

* Wed Jun 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.14-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.13-0
- Autogenerated by Bloom

* Mon Apr 27 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.12-0
- Autogenerated by Bloom

* Sat Apr 25 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.11-0
- Autogenerated by Bloom

* Fri Apr 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.10-0
- Autogenerated by Bloom

* Sun Apr 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.9-0
- Autogenerated by Bloom

* Mon Mar 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.8-0
- Autogenerated by Bloom

* Tue Jan 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.7-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.6-2
- Autogenerated by Bloom

* Tue Dec 23 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.6-1
- Autogenerated by Bloom

