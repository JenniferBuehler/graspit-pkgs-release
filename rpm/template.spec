Name:           ros-indigo-grasp-planning-graspit-msgs
Version:        1.0.0
Release:        0%{?dist}
Summary:        ROS grasp_planning_graspit_msgs package

Group:          Development/Libraries
License:        GPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
Messages for grasp planning with graspit. Some of the messages are later to be
merged with ros-interactive-
manipulation/graspit_simulator/graspit_ros_planning_msgs

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

