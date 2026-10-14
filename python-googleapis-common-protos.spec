Name:		python-googleapis-common-protos
Version:	1.75.5
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/googleapis-common-protos/googleapis_common_protos-%{version}.tar.gz
Summary:	Common protobufs used in Google APIs
URL:		https://pypi.org/project/googleapis-common-protos/
License:	Apache 2.0
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Common protobufs used in Google APIs

%prep
%autosetup -p1
# Cooker python-protobuf provides python3.15dist(protobuf) = 6.32.1.
find . -name pyproject.toml -o -name PKG-INFO | xargs sed -i 's/6\.33\.5/6.32.1/g'

%files
%{py_sitedir}/google
%{py_sitedir}/googleapis_common_protos-*.*-info
