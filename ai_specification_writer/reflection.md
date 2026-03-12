# Reflection on AI-Assisted Specification Writing

## Introduction

Building CarpoolConnect—an enterprise carpooling platform supporting employee commute logistics and corporate ESG sustainability goals—required integrating real-time geo-spatial ride matching, OIDC-compliant authentication, and facility hardware systems. AI-assisted drafting accelerated the specification process but revealed limitations. While AI quickly produced structured documentation, maintaining logical consistency, domain accuracy, and precise technical requirements still demanded human oversight.

## AI Strengths

AI excelled during early drafting, converting rough ideas into structured outputs such as user stories, API descriptions, and preliminary data models. Outputs often reached 70–80% completeness, significantly reducing initial specification time.

The system also demonstrated strong pattern recognition for enterprise architectures. For authentication requirements, it independently suggested single sign-on integration with Okta or Azure AD and outlined user provisioning workflows. It consistently applied structured formats like Role–Goal–Benefit for user stories and produced technical artifacts such as Mermaid.js architecture diagrams.

These strengths were most evident for well-established engineering patterns. Standard REST APIs, authentication workflows, and database schemas were produced clearly and quickly. Simple, pattern-based prompts consistently succeeded—for example, "Draft eight user stories in Role–Goal–Benefit format" yielded high-quality output. In contrast, complex prompts requiring cross-referential logic—like "Ensure all API parameters match Data Model fields"—often failed, highlighting AI's difficulty maintaining coherence across sections.

## AI Weaknesses

Several limitations emerged. Terminology inconsistency was frequent: AI sometimes labeled the same concept as "Ride," "Trip," or "Booking." In practice, this could cause mismatched schemas and implementation errors. Establishing a glossary and anchoring the AI’s role (e.g., "Act as a Senior Systems Architect") with strict negative constraints ("Exclude consumer social features") reduced drift.

Pattern bias also appeared. Even in a defined corporate context, AI sometimes inserted consumer-style features like public profiles, requiring manual removal. Structured prompt templates specifying exact format and tone helped constrain these patterns but did not eliminate human filtering.

Cross-referential prompts were particularly unreliable. Tasks like verifying that API parameters matched data models frequently produced inconsistencies. Improving this would require AI systems to maintain registries of defined terms and constraints for true cross-section validation. Context-aware pattern detection (recognizing "corporate," "SSO," or "ESG") and iterative validation loops ("generate X, then validate Y") could prevent silent inconsistencies in multi-section documents.

## Human Role

Human refinement was essential for reliable specifications. Vague AI outputs like "find nearby matches" required translation into precise constraints, e.g., "within two miles of the commute route and ±30-minute departure window." Humans transformed qualitative goals into quantitative technical parameters.

Abstract features also needed grounding in infrastructure. Concepts like "parking optimization" required specific implementations, such as QR-based access or integration with corporate facility systems. Humans enforced organizational constraints and security standards, and prevented conflation of distinct user needs. For instance, when AI generated requirements for Sustainability Officers and HR Managers together, it merged them into an incoherent dashboard. Humans resolved this by producing separate role-specific specifications and consolidating them intentionally.

## Lessons Learned

Key lessons include: first, define a glossary to prevent terminology drift. Second, generate requirements per persona to avoid mixing unrelated goals. Third, decompose complex prompts into smaller, pattern-based tasks for reliable execution.

Fourth, prompt structure matters: explicit role identity, strict negative constraints, environmental context, and structural templates improve output consistency. Fifth, AI should be treated as a drafting accelerator, not a final authority. While AI rapidly generates structured content, human expertise remains essential for logical consistency, security, and coherent implementation.

Future AI systems that track defined terms, apply context-aware templates, and generate role-separated branches with overlap detection would improve reliability. Until then, human oversight of cross-referential logic remains irreplaceable.