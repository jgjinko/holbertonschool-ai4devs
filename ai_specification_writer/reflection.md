# Reflection on AI-Assisted Specification Writing

## Introduction

The **CarpoolConnect** project is an enterprise-grade commute management platform designed to bridge the gap between employee logistics and corporate sustainability. Creating a technical specification for such a product requires a delicate balance of high-level vision, precise data modeling, and strict security compliance. In this exercise, I utilized AI to transition from a broad conceptual brief to a structured set of technical requirements. This reflection explores the dynamics of that collaboration, identifying where the AI accelerated the process and where human oversight was indispensable to maintain professional standards.


## AI Strengths

AI excels at **rapid structural synthesis** and **boiler-plating**. When provided with a raw product concept, the AI was able to immediately categorize information into standardized industry formats like "User Stories" and "API Endpoints." This "cold start" capability is perhaps the AI's greatest asset; it eliminates the "blank page" problem by providing a 70-80% complete draft in seconds.

Specifically, the AI was highly effective at:
* **Syntax Enforcement**: Consistently applying the "As a [role], I want [goal], so that [benefit]" template.
* **Visual Mapping**: Generating Mermaid.js code for system architecture diagrams, which would otherwise require specialized design software and manual layout.
* **Mathematical Precision**: Using LaTeX for variables like $CO_2$ and range constraints like $\pm 30$ minutes ensured that technical nuances were represented formally rather than in plain, ambiguous text.


## AI Weaknesses

The primary weakness observed was **contextual drift and "hallucinated bloat."** AI tends to prioritize linguistic patterns over strict logical constraints. For example, when asked for a specific number of user types or features, the AI often "over-delivered" by including generic features (like "Ratings and Reviews") that were not central to the specific *corporate* focus of CarpoolConnect.

Another significant failure was **terminological inconsistency**. In early drafts, the AI interchangeably used "Ride," "Trip," and "Offer" in different sections. While a human reader might infer they are the same, in a technical specification, this lack of "Domain Isolation" is a critical failure. If a Data Model defines a `Trip` but the API refers to a `Ride`, the resulting code would be broken. AI treats each response as an independent text-generation task rather than a unified, internally consistent document.


## Human Role

Human refinement was critical in **filtering for intent** and **enforcing constraints**. I had to act as the "Curator of Logic," stripping away the AI's tendency toward genericism to focus on the unique differentiators of the product, such as the "SSO Walled Garden" and "Facility Integration."

Critical manual interventions included:
* **Parameter Definition**: Refining vague AI goals like "nearby matches" into testable acceptance criteria like "within a 2-mile radius."
* **Strategic Alignment**: Ensuring that the "Sustainability Officer" user stories focused specifically on ESG reporting rather than general social features.
* **Constraint Management**: Explicitly instructing the AI to remove redundant features to meet the "MVP-first" requirement.


## Lessons Learned

In real-world specification writing, the most effective prompt types are **Iterative and Constrained**. 
* **Easier Prompts**: Broad structural requests (e.g., "Draft a system architecture for a carpool app") produce high-quality initial results.
* **Harder Prompts**: Specific logic-based requests (e.g., "Ensure the API parameters exactly match the User Data Model") often require multiple rounds of correction.

**Success Example**: The AI perfectly mapped the relationship between the Auth Service and corporate Identity Providers (OIDC/SAML) without needing a detailed explanation of enterprise security.
**Failure Example**: The AI initially failed to recognize that "Parking Optimization" required a separate data link to facility gate hardware, treating it as a purely software-based notification.

**Future Improvements**: To improve AI-assisted specs, one should provide a **"Glossary of Terms"** at the start of the session to prevent terminological drift. Furthermore, using "Chain of Thought" prompting—asking the AI to explain its logic for a data model before writing the API—helps ensure the two remain functionally linked.