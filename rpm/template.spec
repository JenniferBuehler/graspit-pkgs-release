Name:           ros-indigo-grasp-planning-graspit-ros
Version:        1.2.0
Release:        0%{?dist}
Summary:        ROS grasp_planning_graspit_ros package

Group:          Development/Libraries
License:        GPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-grasp-planning-graspit
Requires:       ros-indigo-grasp-planning-graspit-msgs
Requires:       ros-indigo-manipulation-msgs
Requires:       ros-indigo-roscpp
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-grasp-planning-graspit
BuildRequires:  ros-indigo-grasp-planning-graspit-msgs
BuildRequires:  ros-indigo-manipulation-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslint

%description
ROS services for the grasp_planning_graspit package

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
* Sat Jan 06 2018 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 1.2.0-0
- Autogenerated by Bloom

* Fri Jan 05 2018 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 1.1.3-0
- Autogenerated by Bloom

* Sun Aug 07 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 1.1.2-0
- Autogenerated by Bloom

* Wed Jun 08 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 1.0.0-0
- Autogenerated by Bloom

* Sat Apr 02 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.1.5-0
- Autogenerated by Bloom

* Thu Mar 10 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.1.4-0
- Autogenerated by Bloom

* Tue Mar 08 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.1.3-0
- Autogenerated by Bloom

* Fri Mar 04 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

* Wed Mar 02 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

