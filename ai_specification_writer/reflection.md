# Reflection on AI-Assisted Specification Writing


## Introduction

The CarpoolConnect project represents a complex intersection of logistics, enterprise security, and sustainability reporting. Developing a comprehensive specification for such a platform requires balancing high-level business goals (ESG targets) with granular technical constraints (SOC 2 compliance and geo-spatial matching). In this exercise, AI served as a primary drafting partner, translating a broad project concept into structured user stories, data models, and API definitions.


## AI Strengths

The most significant strength of AI in this process was its ability to perform **rapid structural synthesis**. When provided with the initial project brief, the AI instantly categorized information into logical domains: User Types, Core Features, and Technical Constraints. 

AI excelled in **standardized formatting**. For example, generating a Mermaid system architecture diagram from a text description is a task that would take a human significantly longer to manually align. Furthermore, the AI was highly effective at maintaining the "Role-Goal-Benefit" syntax for user stories. It acted as a powerful "blank page" killer, providing a 70-80% complete draft that allowed for immediate critique rather than slow creation. Its ability to maintain consistent LaTeX-style formatting for scientific variables, such as $CO_2$ or mathematical ranges like $\pm 30$ minutes, added a layer of professional polish to the technical sections.


## AI Weaknesses

Despite its speed, the AI displayed a tendency toward **genericism and "feature creep."** In the initial drafts, the AI included four or five user types and six or more features when the prompt only required a specific subset. This "over-delivery" often obscures the core MVP (Minimum Viable Product) requirements, making the specification feel bloated rather than focused.

A second weakness was **contextual drift in technical naming**. While the AI understood the *concept* of a "Ride," it occasionally swapped terminology between "Trip," "Offer," and "Carpool" across different sections (Data Models vs. APIs). Without human intervention, these inconsistencies could lead to significant confusion during the implementation phase, as developers might interpret these as distinct entities rather than a single unified object.


## Human Role

Manual refinement was critical in **editing for precision and constraint enforcement**. The "Refined" version of the specifications shows that while the AI can describe a feature, a human is needed to define the *parameters* of that feature (e.g., changing "nearby" to "within a 2-mile buffer"). 

I had to step in to ensure **domain isolation**. The AI often blended the needs of the "Sustainability Officer" with the "HR Manager." I had to separate these into distinct user stories to ensure the acceptance criteria were testable. For instance, a Sustainability Officer needs "verifiable PDF reports for ESG disclosure," whereas an HR Manager needs "employee satisfaction metrics." The human role is to act as the "Curator of Intent," stripping away the AI's polite filler text to reveal the hard technical requirements underneath.


## Lessons Learned
Using AI for real-world specification writing provides several key takeaways:

1.  **Iterative Prompting is Mandatory**: You cannot expect a perfect "one-shot" specification. The best results came from providing a broad context, then using follow-up prompts to "Refine," "Simplify," or "Compare."
2.  **The "80/20" Rule**: AI is brilliant for the first 80% of the work—the structure, the boilerplate code, and the general logic. The final 20%—the specific business rules and security edge cases—requires 100% human oversight.
3.  **Strict Boundary Setting**: To avoid AI-generated bloat, prompts must include hard constraints (e.g., "Provide exactly 3 features" or "Use only 2 user types").
4.  **Consistency Checks**: Always perform a final pass to ensure that a variable name in the Data Model matches the endpoint parameter in the API section. AI treats these as independent text-generation tasks, whereas a spec requires them to be functionally linked.

In conclusion, AI is an exceptional "Drafting Engine" that shifts the human role from *writer* to *editor*. This transition significantly accelerates the development lifecycle, provided the human editor remains vigilant against the AI's tendency toward generic and inconsistent outputs.