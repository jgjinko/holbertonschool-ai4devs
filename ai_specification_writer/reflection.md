# Reflection on AI-Assisted Specification Writing

## Introduction
Building CarpoolConnect—an enterprise carpooling platform supporting employee commute logistics and corporate ESG goals—required integrating real-time geo-spatial ride matching, OIDC-compliant authentication, and facility hardware systems. AI-assisted drafting accelerated the specification process but revealed limitations. While AI produced structured documentation quickly, maintaining logical consistency, domain accuracy, and precise technical requirements still required human oversight.

## AI Strengths
AI excelled in early drafting, converting rough ideas into structured outputs such as user stories, API descriptions, and preliminary data models. Outputs often reached 70–80% completeness, reducing the time needed for initial specifications.

The system also demonstrated strong pattern recognition for enterprise architectures. For authentication requirements, AI suggested single sign-on with Okta or Azure AD and outlined user provisioning workflows. It consistently applied structured templates like Role–Goal–Benefit for user stories and produced technical artifacts such as Mermaid.js diagrams.

Strengths were most evident for well-established engineering patterns. Standard REST APIs, authentication workflows, and database schemas were generated clearly and quickly. Simple, pattern-based prompts consistently succeeded—for example, "Draft eight user stories in Role–Goal–Benefit format" produced high-quality output. Complex prompts requiring cross-sectional logic—like "Ensure all API parameters match data model fields"—often failed, revealing AI’s difficulty maintaining coherence across sections.

## AI Weaknesses
Terminology inconsistency was frequent: the AI sometimes labeled the same concept as "Ride," "Trip," or "Booking," risking schema misalignment. Prompt structure influenced output quality significantly. Explicit role identity ("Act as a Senior Systems Architect"), environmental context ("closed corporate platform with SSO"), strict negative constraints ("Exclude consumer social features"), and structural templates ("[Role], [Goal], [Benefit]") all improved consistency. When omitted, AI reverted to generic patterns and introduced bias.

Pattern bias also appeared. Even in closed corporate contexts, AI occasionally suggested consumer-style features like public profiles. Structured prompts reduced, but did not eliminate, the need for human filtering. Vague outputs, like "parking optimization," required translation into measurable parameters: "QR-based access integration with corporate facility systems" or "within two miles of commute route and ±30-minute window."

Cross-referential validation was unreliable. Tasks like verifying that API parameters matched data models frequently produced inconsistencies. Future improvements could include specification registries tracking terms, context-aware pattern detection to constrain output, iterative generate-and-validate loops, and role-separated branches with automatic overlap detection to prevent conflation.

## Human Role
Human refinement was essential. Vague AI outputs, such as "find nearby matches," needed translation into precise constraints. Humans grounded abstract features like "parking optimization" in infrastructure, enforced organizational constraints and security standards, and prevented conflation of distinct user needs. For example, generating requirements for Sustainability Officers and HR Managers together produced incoherent outputs; humans resolved this by creating separate persona-specific specifications and consolidating them afterward.

## Lessons Learned
Key lessons include: first, define a glossary to prevent terminology drift. Second, generate requirements per persona independently to avoid conflating distinct needs. Third, decompose complex prompts into smaller, pattern-based tasks for reliability.

Prompt structure profoundly influences AI output quality. Explicit role identity, environmental context, strict negative constraints, and structured templates together reduce pattern bias and maintain consistency. When applied correctly, AI can accelerate drafting and produce high-quality boilerplate content; when omitted, outputs revert to consumer-style assumptions.

Finally, AI is best used as a drafting accelerator, not a final authority. Human expertise remains essential for logical coherence, security compliance, and translating vague business goals into precise technical requirements. Future systems that maintain specification registries, implement context-aware template matching, and generate role-separated outputs with overlap detection could improve reliability. Until then, human oversight of cross-referential logic remains essential.