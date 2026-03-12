# Reflection on AI-Assisted Specification Writing

## Introduction
Building CarpoolConnect—an enterprise carpooling platform designed to support employee commute logistics while advancing corporate ESG sustainability goals—required integrating real-time geo-spatial ride matching, OIDC-compliant authentication, and facility hardware systems. Using AI to help draft the system specifications accelerated the writing process but also revealed important limitations. While AI generated structured drafts quickly, maintaining logical consistency, domain accuracy, and precise requirements still required significant human oversight.

## AI Strengths
AI was most effective during the early drafting phase of the specification process. It quickly transformed rough ideas into structured documentation, including user stories, API endpoint descriptions, and preliminary data models. In many cases the generated content reached roughly 70–80% completeness, which significantly reduced the time needed to create an initial specification.

The system also demonstrated strong pattern recognition for common enterprise software architectures. For example, when describing authentication requirements, the AI independently suggested single sign-on integration with enterprise identity providers such as Okta or Azure AD and outlined user provisioning flows. It also consistently generated structured user stories using the Role–Goal–Benefit format and was able to produce technical artifacts such as architecture diagrams using Mermaid.js syntax.

These strengths were most evident when the task relied on widely documented software engineering patterns. Standard REST API structures, authentication workflows, and typical database schemas were generated clearly and efficiently with minimal prompting. This ability made AI particularly valuable for producing the structural foundation of the specification.

## AI Weaknesses
Despite these strengths, several weaknesses became clear during the process. One recurring issue was terminology inconsistency. The AI sometimes used multiple labels—such as “Ride,” “Trip,” and “Booking”—to describe the same concept across different sections. In a real implementation, this type of drift could lead to mismatched data models, inconsistent APIs, and confusion during development. The problem occurs because the model generates text probabilistically rather than maintaining a persistent conceptual model of the system.

Another limitation was pattern bias. Even when the project context was clearly defined as a closed corporate platform, the AI occasionally introduced features typical of consumer applications, such as public user profiles or social features. These additions were inappropriate for an enterprise system and had to be removed manually.

A more significant limitation appeared when prompts required cross-referencing information between sections. When asked to verify that API parameters matched data model fields, the AI often produced inconsistencies. Maintaining alignment across multiple parts of a technical specification proved difficult because the model cannot reliably validate earlier generated content.

## Human Role
Human refinement was essential for transforming AI-generated drafts into usable specifications. Many AI outputs were conceptually correct but lacked measurable detail. For instance, vague requirements such as “find nearby matches” needed to be translated into precise rules like “within two miles of the commute route and within a ±30-minute departure window.”

Humans also grounded abstract features in real operational systems. A concept like “parking optimization” required clarification through concrete implementations, such as QR-based parking access or integration with corporate parking infrastructure.

In addition, human review ensured that organizational and security constraints were applied consistently across the document. While AI helped generate structure and ideas, humans were responsible for enforcing enterprise requirements, removing irrelevant features, and maintaining logical coherence throughout the specification.

## Lessons Learned
Several practical lessons emerged from using AI to support specification writing. First, defining a clear glossary of system terminology before generating content helps prevent naming inconsistencies across sections. Second, requirements for different user personas should be generated separately to avoid mixing unrelated goals or metrics.

Third, complex prompts that require cross-document validation should be broken into smaller steps rather than handled in a single request. AI performs better when tasks are independent and pattern-based rather than logically interdependent.

Providing strong contextual constraints in prompts also improves output quality. Explicitly stating that the system operates in a closed corporate environment with SSO authentication helps prevent the AI from defaulting to consumer-application patterns.

Overall, the most effective approach is to treat AI as a drafting accelerator rather than a decision-maker. AI can rapidly generate structured documentation and technical scaffolding, but human expertise remains necessary for logic, security considerations, precise constraints, and ensuring the final specification is coherent and implementable.