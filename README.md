# Repository Directory Structure Enforcement

## 📌 Overview
This repository enforces a strict directory structure to ensure compliance with organizational policies. A GitHub Action automatically validates the structure on every pull request (PR) using a Python script. Additionally, changes to specific directories require approval from the security team.

## 📂 Directory Structure Rules
1. **Top-level directories must be named with a 12-digit AWS account number.**
2. **Inside each AWS account directory, the following subdirectories are allowed:**
   - `network_firewall_policy`
   - `permissionboundary_policy`
3. **Any file may be created inside these directories.**
4. **No other directories are allowed at the top level or inside the AWS account directories.**

## 🚀 Automated Validation
A GitHub Action runs on every PR to validate the directory structure using the [`check_directory_structure.py`](.github/scripts/check_directory_structure.py) script. The validation checks:
- All top-level directories are **exactly** 12-digit numbers.
- Only the `network_firewall_policy` and `permissionboundary_policy` directories exist inside them.
- Any other directory structure is **rejected.**

If the validation fails, the PR will be blocked until the structure is corrected.

## 🔐 Security Team Approval Requirement
- If a PR **modifies, adds, or removes** the `network_firewall_policy` or `permissionboundary_policy` directories, it will **require approval from the security team** before merging.
- This is enforced using a **GitHub CODEOWNERS file** and **branch protection rules**.
- Without security team approval, the PR cannot be merged.

## 🛠 How to Fix Validation Errors
If your PR fails the directory structure check:
1. Ensure that your top-level directory is a **12-digit AWS account number**.
2. Only create `network_firewall_policy` or `permissionboundary_policy` inside that directory.
3. Remove any unauthorized directories.
4. If modifying security-sensitive directories, request a **security team review.**

## ✅ Example of a Valid Structure
```
123456789012/   <-- AWS Account Directory (valid 12-digit number)
│-- network_firewall_policy/   <-- Allowed subdirectory
│   ├── firewall_rules.json
│-- permissionboundary_policy/  <-- Allowed subdirectory
│   ├── policy_config.yaml
```

## ❌ Example of an Invalid Structure
```
not_a_number/   <-- ❌ INVALID: Must be a 12-digit AWS account number
aws-account-123/ <-- ❌ INVALID: Must be a 12-digit AWS account number
123456789012/
│-- unauthorized_dir/   <-- ❌ INVALID: Only specific subdirectories allowed
│-- network_firewall_policy/
│   ├── config.json
654321/   <-- ❌ INVALID: Not a 12-digit AWS account number
```

For questions or exceptions, please contact the security team. 🚀

