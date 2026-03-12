# Reflection on AI-Assisted Specification Writing

## Introduction

Building CarpoolConnect—an enterprise carpooling platform combining employee logistics with corporate ESG sustainability targets—required integrating real-time geo-spatial matching, OIDC-compliant authentication, and facility hardware integration. This project tested the boundaries of AI-assisted specification writing, revealing where generative AI excels and where human expertise remains irreplaceable.

## AI Strengths

AI proved exceptional at rapid structural scaffolding, eliminating the "blank page" problem. Within seconds, it synthesized rough ideas into polished User Stories, API endpoints, and Data Models at approximately 75% completion. The AI demonstrated impressive pattern recognition for enterprise domains: it independently identified SSO integration with Okta/Azure AD, maintained consistent Role-Goal-Benefit formatting for user stories, applied scientific notation ($CO_2$ emissions, ±30 minutes precision), and generated Mermaid.js architecture diagrams—typically requiring specialized design tools.

For well-established patterns found abundantly in training data, AI delivered excellent results without detailed guidance. Enterprise authentication architectures, standard REST APIs, and common database schemas all benefited from this "pre-trained domain knowledge."

## AI Weaknesses

Two critical failure modes emerged. First: **terminological drift**. The AI inconsistently labeled the same concept as "Ride," "Trip," and "Booking" across different specification sections—a production catastrophe causing schema misalignment and frontend confusion. This stems from the AI processing text as independent statistical distributions rather than unified logical models.

Second: **pattern bias and feature bloat**. Despite explicit enterprise constraints, AI inserted generic consumer-app features like "public user profiles" that contradicted the secure corporate context. The system defaulted to common training patterns rather than respecting domain-specific constraints.

Third: **cross-referential validation failure**. When asked to "Ensure API parameters match data model definitions," AI produced inconsistent results. It struggles with backward-looking consistency checks across technical domains—a fundamental limitation for specifications requiring logical coherence across sections.

## Prompt Types: Easier vs. Harder Prompts

Output quality directly correlated with prompt structure complexity. **Easier prompts** (broad, pattern-based requests) succeeded consistently. Example: "Draft 8 user stories in Role-Goal-Benefit format for a carpooling application" produced professional, consistent output at ~80% completion. These succeed because they leverage well-defined linguistic templates that don't require cross-referential memory.

**Harder prompts** (logic-intensive, inter-dependent validation) consistently failed. Example: "Ensure all API endpoint parameters match the Data Model primary keys defined in Section 3" produced misaligned results. The AI cannot maintain coherence across document sections or "look back" to validate consistency.

Key actionable insight: Decompose complex requests into standalone, pattern-based prompts rather than attempting validation across sections in single requests.

## Real-World Success and Failure Examples

**Success Case**: The AI perfectly synthesized authentication requirements, independently identifying SSO integration with Okta and Azure AD, including automatic user provisioning workflows. I provided minimal guidance—just the domain context. This succeeded because enterprise SSO is a well-established pattern in training data.

**Failure Case**: When asked to generate requirements for both Sustainability Officers and HR Managers simultaneously, the AI conflated distinct needs—merging $CO_2$ aggregate reporting (for ESG) with satisfaction metrics (for HR) into a single incoherent dashboard. Root cause: the system cannot distinguish between semantically different contexts when multiple personas are mentioned. Solution: generate separate specifications per role, then consolidate intentionally.

## Human Role: The Essential Gatekeeper

Manual refinement was essential and frequent. When AI vaguely suggested "finding nearby matches," I quantified it: "within 2 miles of the commute path." When "Parking Optimization" remained ambiguous, I anchored it to concrete facility hardware and QR codes. Humans translated qualitative business goals into quantitative technical requirements while enforcing security boundaries the AI overlooked.

The most critical insight: avoid asking AI to consolidate multiple user personas in single prompts. When I asked AI to generate requirements for both Sustainability Officers (needing aggregate $CO_2$ data) and HR Managers (needing satisfaction metrics), it merged these into a single incoherent dashboard. Humans solved this by generating separate specifications per role, then intentionally consolidating.

## Key Prompt Elements for High-Fidelity Specifications

Four pillars proved critical for quality output:

1. **Role Identity**: Define context like "Act as a Senior Systems Architect" to anchor perspective.
2. **Environmental Context**: Specify boundaries—"closed-loop corporate environment with SSO"—to prevent consumer-app assumptions.
3. **Strict Constraints**: Use negative constraints—"exclude generic social media functions"—to fight pattern bias.
4. **Structural Templates**: Specify formatting—"[Role], [Goal], [Benefit]"—to ensure consistency.

These elements directly improved output quality. When I applied all four pillars, terminology remained consistent across sections. When omitted, the AI reverted to generic patterns. Environmental context proved most powerful—specifying "closed-loop corporate environment" explicitly constrained the AI away from consumer-facing assumptions that plagued early iterations.

## Future Improvements for AI Systems

Based on observed limitations:

1. **Consistency Registries**: Maintain a registry tracking defined terms and constraints to enable cross-referential validation.
2. **Context-Aware Patterns**: Detect domain markers ("corporate," "SSO") to constrain pattern selection beyond consumer defaults.
3. **Role Separation**: Generate distinct branches per persona, flagging overlaps for human consolidation.
4. **Validation Loops**: Structure prompts as "generate X, then validate against Y" with failure reporting.

## Lessons Learned

**For effective AI-assisted specifications:**

1. **Build glossaries first**—Define immutable terminology before generation to prevent drift across sections.

2. **Separate by persona**—Generate user stories and requirements per role independently, then consolidate manually to avoid conflation.

3. **Decompose inter-dependent requests**—Avoid single prompts validating cross-document consistency; instead, generate separately and assign humans to verify alignment.

4. **Anchor with constraints**—Explicitly exclude generic features and specify exact formatting to fight pattern bias.

5. **Reserve human cognition for logic**—Let AI handle boilerplate; reserve human expertise for security boundaries, quantifying vague requirements, and ensuring technical coherence.

## Conclusion

AI is a powerful accelerant, not a replacement. The most effective specifications leverage AI's speed for structural work while maintaining humans as architects of logic, security, and domain precision. CarpoolConnect succeeded because of this hybrid approach.