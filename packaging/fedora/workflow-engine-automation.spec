Name:           workflow-automation-engine
Version:        beta
Release:        1%{?dist}
Summary:        Workflow automation engine

License:        AGPLv3
URL:            https://github.com/HugoCornelis/workflow-automation-engine
Source0:        https://github.com/HugoCornelis/workflow-automation-engine/archive/refs/heads/master.zip

BuildRequires:  
Requires:       

%description


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Tue Feb 03 2026 Super User
- 
