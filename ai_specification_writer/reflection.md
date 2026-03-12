# Reflection on AI-Assisted Specification Writing

## Introduction
Building CarpoolConnect—an enterprise carpooling platform supporting employee commute logistics and corporate ESG goals—required integrating real-time geo-spatial ride matching, OIDC-compliant authentication, and facility hardware systems. AI-assisted drafting accelerated the specification process but revealed limitations. While AI produced structured documentation quickly, maintaining logical consistency, domain accuracy, and precise technical requirements still required human oversight.

## AI Strengths
AI excelled in early drafting, converting rough ideas into structured outputs such as user stories, API descriptions, and preliminary data models—often reaching 70–80% completeness. The system demonstrated strong pattern recognition for enterprise architectures, suggesting single sign-on with Okta or Azure AD and outlining user provisioning workflows. It consistently applied Role–Goal–Benefit templates and produced Mermaid.js diagrams.

**Easier vs Harder Prompt Types**: Easier prompts succeeded consistently—"Draft eight user stories in Role–Goal–Benefit format" yielded ~80% completion. Harder prompts (logic-intensive, inter-dependent validation) failed. Example: "Ensure API parameters match data model keys" produced misaligned results, revealing AI's inability to maintain coherence across sections.

## AI Weaknesses
**Success Example**: Designing SSO architecture with Okta/Azure AD succeeded because enterprise SSO is well-established in training data. **Failure Example**: Requesting requirements for both Sustainability Officers and HR Managers caused AI to conflate $CO_2$ aggregate reporting (ESG need) with satisfaction metrics (HR need) into an incoherent dashboard.

Terminology inconsistency was frequent: AI labeled identical concepts as "Ride," "Trip," or "Booking" across sections, causing schema misalignment. Prompt structure significantly influenced quality. Explicit role identity ("Senior Systems Architect"), environmental context ("closed corporate with SSO"), strict negative constraints ("Exclude consumer features"), and structural templates ("[Role], [Goal], [Benefit]") all improved consistency. When all four were applied, terminology remained stable; when omitted, AI reverted to generic patterns.

Pattern bias manifested as consumer-style features even in corporate contexts. Vague outputs like "parking optimization" required translation into measurable parameters: "QR-based access integration with facility systems" or "within two miles of commute route and ±30-minute window."

Cross-referential validation was unreliable. Future improvements: maintain specification registries; implement context-aware pattern detection recognizing "corporate," "SSO," "ESG"; structure iterative validation loops as "generate X, validate Y"; generate role-separated branches with automatic overlap flagging.

## Human Role
Human refinement was essential. Vague outputs needed translation into precise constraints. Humans grounded abstract features in infrastructure, enforced organizational constraints, and prevented persona conflation by creating separate role-specific specifications and consolidating them afterward.

## Lessons Learned
First, define a glossary to prevent drift. Second, generate requirements per persona independently. Third, decompose complex prompts into smaller tasks. Prompt structure profoundly influences quality: explicit role, environmental context, strict constraints, and templates together reduce bias and maintain consistency. When applied, AI accelerates drafting; when omitted, outputs revert to generic assumptions. AI is best used as a drafting accelerator, not a final authority. Human expertise remains essential for logical coherence, security, and translating vague goals into precise requirements.