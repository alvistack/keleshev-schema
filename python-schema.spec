# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-schema
Epoch: 100
Version: 0.7.5
Release: 1%{?dist}
BuildArch: noarch
Summary: Simple data validation library
License: MIT
URL: https://github.com/keleshev/schema/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
schema is a library for validating Python data structures, such as those
obtained from config-files, forms, external services or command-line
parsing, converted from JSON/YAML (or something else) to Python
data-types.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-schema
Summary: Simple data validation library
Requires: python3
Requires: python3-contextlib2 >= 0.5.5
Provides: python3-schema = %{epoch}:%{version}-%{release}
Provides: python3dist(schema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-schema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(schema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-schema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(schema) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-schema
schema is a library for validating Python data structures, such as those
obtained from config-files, forms, external services or command-line
parsing, converted from JSON/YAML (or something else) to Python
data-types.

%files -n python%{python3_version_nodots}-schema
%license LICENSE-MIT
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-schema
Summary: Simple data validation library
Requires: python3
Requires: python3-contextlib2 >= 0.5.5
Provides: python3-schema = %{epoch}:%{version}-%{release}
Provides: python3dist(schema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-schema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(schema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-schema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(schema) = %{epoch}:%{version}-%{release}

%description -n python3-schema
schema is a library for validating Python data structures, such as those
obtained from config-files, forms, external services or command-line
parsing, converted from JSON/YAML (or something else) to Python
data-types.

%files -n python3-schema
%license LICENSE-MIT
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-schema
Summary: Simple data validation library
Requires: python3
Requires: python3-contextlib2 >= 0.5.5
Provides: python3-schema = %{epoch}:%{version}-%{release}
Provides: python3dist(schema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-schema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(schema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-schema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(schema) = %{epoch}:%{version}-%{release}

%description -n python3-schema
schema is a library for validating Python data structures, such as those
obtained from config-files, forms, external services or command-line
parsing, converted from JSON/YAML (or something else) to Python
data-types.

%files -n python3-schema
%license LICENSE-MIT
%{python3_sitelib}/*
%endif

%changelog
