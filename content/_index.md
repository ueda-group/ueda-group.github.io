---
# Leave the homepage title empty to use the site title
title: Ueda Group
summary: ''
date: 2022-10-24
type: landing

sections:

  # =========================================================
  # HERO
  # =========================================================
  - block: hero
    content:
      title: Ueda Group
      text: |-
        Quantum Many-Body Physics, Tensor Networks, and Quantum Algorithms
        <br><br>
        We develop theoretical, numerical, and quantum-classical hybrid approaches for understanding quantum systems and designing quantum algorithms.

      primary_action:
        text: Research
        url: research/

      secondary_action:
        text: Publications
        url: publications/

    design:
      background:
        gradient_mesh:
          enable: true

  # =========================================================
  # RESEARCH OVERVIEW
  # =========================================================
  - block: markdown
    content:
      title: Research
      subtitle: ''
      text: |-
        The Ueda Group focuses on tensor network methods, quantum many-body physics, quantum algorithms, and quantum-classical hybrid computation.

        We develop numerical and theoretical methods for strongly correlated systems, quantum entanglement, variational quantum computation, and quantum-HPC hybrid workflows.

        Our research connects condensed matter physics, quantum information, and high-performance computing.

    design:
      columns: '1'

  # =========================================================
  # RESEARCH TOPICS
  # =========================================================
  - block: markdown
    content:
      title: Research Topics
      subtitle: ''
      text: |-
        - **Tensor Networks:** Development and optimization of tensor network methods for quantum and classical many-body systems.

        - **Quantum Algorithms:** Design of quantum algorithms inspired by entanglement structures and tensor network representations.

        - **Quantum-Classical Hybrid Computation:** Variational quantum algorithms, tensor-network ansätze, and hybrid workflows for near-term quantum devices.

        - **Quantum HPC:** Integration of quantum computing, high-performance computing, and numerical many-body methods.

    design:
      columns: '1'

  # =========================================================
  # PUBLICATIONS
  # =========================================================
  - block: collection
    content:
      title: Recent Publications
      text: ''
      count: 5

      filters:
        folders:
          - publications

        exclude_featured: false

    design:
      view: citation

  # =========================================================
  # TALKS
  # =========================================================
  - block: collection
    id: talks
    content:
      title: Upcoming Talks

      filters:
        folders:
          - events

        exclude_past: true

    design:
      view: card

  # =========================================================
  # NEWS
  # =========================================================
  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ''
      text: ''

      page_type: news
      count: 10

      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''

      offset: 0
      order: desc

    design:
      view: card

      spacing:
        padding: [0, 0, 0, 0]
---