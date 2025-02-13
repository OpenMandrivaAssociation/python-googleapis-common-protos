Name:		python-googleapis-common-protos
Version:	1.67.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/googleapis-common-protos/googleapis_common_protos-%{version}.tar.gz
Summary:	Common protobufs used in Google APIs
URL:		https://pypi.org/project/googleapis-common-protos/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Common protobufs used in Google APIs

%files
%{py_sitedir}/google
%{py_sitedir}/googleapis_common_protos-*.*-info
