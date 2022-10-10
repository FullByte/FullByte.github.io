# CAF and WAF

## Cloud Adoption Framework Steps

### Strategy

Business justification & outcomes

1. Motivations → Why move? (migration, innovation)
2. Success Measurements → Savings/New markets/Revenue/...
3. Business Justification → ROI → Business Case (Motivations + Measurements = Business Justification) → MS Helpers: Azure TCO calc, Azure Pricing Calc, Azure Cost Management
4. First Project:

   - Business Criteria (Should already work (not WIP/Prototype/new Project), dedicated owner, strong motivation to move
   - Technical Criteria (minimum dependencies)

### Planning

CAF 1 Stage: Actionable plan

5. Digital Estate (Asset Inventory) → 5 Rs Rationalization:

   - Rehost → move to cloud without any changes (IaaS)
   - Refaktor → small changes to make it fit in Azure e.g. IaaS VM + Paas DB + PaaS Webserver
   - Rearchict → Introduce new technologies e.g. Key Vault, Backup Process, ...
   - Rebuild → Effort to do above is to high/not worth it → start new
   - Replace → What does the cloud has to offer already → Maybe Azure replaces your app with an SaaS solution

6. Initial Organization Alignment (every one of relevance/importance needs to agree on moving to the cloud)
7. Skills readiness plan → review current skill set → create plan to address gaps (new skills required)
8. Cloud Adoption Plan = Digital Estate + Initial Organization Alignment + Skills readiness plan

### Readiness

CAF 2 Stage: Prepare Azure Environment

9. Azure Setup Guide → Read Docs → How do you want your environment to look like
10. Azure Landing Zone → Create Environment → Code Base → IaC
11. Extend Landing Zone → Expand for further cloud transition
12. Check Best Practices → Hard to change later, do it right

### Adopt

CAF 3 Stage: Implement → migrate & innovate

13. Migrate

    - First Migration
    - Migration Szenarios (OS, App, Data, Other)
    - best practices → tool check/design check/process check
    - migration process improvement → eval current migration steps and improve where possible

14. Innovate

    - Business Value Consensus → Value/needs vs. cloud strategy
    - Innovation Guide → MVP
    - best practices
    - process improvement

### Overall Management Processes

Governance (overall process)

    - comply, control and secure
    - Define gouvernance solutions → Business needs, agility, control risks

Management (overall process)

    - Operate & Optimize
    - Manage cloud environment (Cloud operations) → Stability & Control Costs

Organize

    - Roles and Responsiblites (RACI)

### Links

- Good Video Summery: <https://www.youtube.com/watch?v=d6usiB4MKq8>
- Cloud Adoption Framework Source: <https://github.com/microsoft/CloudAdoptionFramework>
- MS LearN: <https://docs.microsoft.com/en-us/learn/modules/microsoft-cloud-adoption-framework-for-azure>
- Official Page: <https://azure.microsoft.com/en-us/cloud-adoption-framework/>
- Official Docs: <https://docs.microsoft.com/en-us/azure/cloud-adoption-framework>
