#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Basic Information
AUTHOR = "Lucien Piat"
SITENAME = "Lucien Piat"
SITESUBTITLE = "Bioinformatics Engineer | Genome assembly & pangenomics"
SITEDESCRIPTION = "Lucien Piat - Bioinformatician | Bordeaux, France"
SITEURL = "https://lucienpiat.fr"

PATH = "content"
TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"

# Theme
THEME = "themes/portfolio"

# Profile
PROFILE_IMAGE = "images/profile.png"
AUTHOR_EMAIL = "lucienpiat33@gmail.com"
AUTHOR_LOCATION = "Bordeaux, France"
FAVICON = "images/favicon.ico"

# Social Links
GITHUB_URL = "https://github.com/Lucien-Piat"
LINKEDIN_URL = "https://www.linkedin.com/in/lucien-piat-47930419b/"


# About Section
ABOUT_ME = """
I'm a <b>Bioinformatics Engineer</b> currently working at Agroscope (Switzerland) on de novo genome assembly and genetic diversity in grass ecotypes. I recently completed my M.Sc. in Bioinformatics from the University of Rouen, with an 18-month apprenticeship at INRAE.<br><br>

My work centers on <b>pangenomics, genome assembly, and NGS analysis</b>, where I develop computational tools and workflows for large-scale genomic data. These are topics I'm eager to explore further and at greater depth.<br><br>

I also served as House Manager at the Bordeaux National Opera for five years, coordinating reception teams during evening performances, a role that taught me rigor, teamwork, and attention to detail.
"""
# Skills Section
SKILLS = {
    "Bioinformatics": ["Genome Assembly ⋆", "Pangenomics ⋆", "NGS", "Workflow Development", "Structural Variants"],
    "Programming": ["Python ⋆", "Snakemake ⋆", "Bash", "R", "LaTeX"],
    "DevOps & HPC": ["Apptainer ⋆", "Cluster Computing", "SLURM, Hetzner", "Git", "CI/CD"],
}

# Projects Section
PROJECTS = [
    {
        "name": "MSpangepop ⋆",
        "description": "Python library for pangenome simulation under coalescent demographic models. Features clean, object-oriented architecture designed for extensibility and ease of use by biologists.",
        "pi": "DSc Ludovic Duvaux",
        "tech": ["Python", "Population Genetics", "Coalescent Theory", "OOP", "MSprime / tskit", "Pangenome Graphs"],
        "github": "https://github.com/inrae/MSpangepop",
        "gitlab": "https://forge.inrae.fr/pangepop/MSpangepop/",
        "extra": ("Poster", "pdfs/02_Piat_et_al_Jul_2025.pdf"),
        "images": ["images/mspangepop_A.svg"],
    },
    {
        "name": "Asm4gp ⋆",
        "description": "Comprehensive long-read assembly and QC pipeline supporting PacBio, ONT, TRIO, Hi-C, and HiFi data. Developed using Snakemake to automate haplotype-resolved genome assembly inputs for pangenome construction.",
        "pi": "DSc Ludovic Duvaux",
        "tech": ["Snakemake", "Python", "SLURM", "Apptainer", "Conda", "Bash"],
        "github": "https://github.com/inrae/GenomAsm4pg",
        "gitlab": "https://forge.inrae.fr/asm4pg/GenomAsm4pg/",
        "extra": ("Annimated flowchart", "https://asm4pg-animated-7dc863.pages-forge.inrae.fr/asm4pg_animated.html"),
        "images": ["images/asm4pg_A.png", "images/asm4pg_B.png"],
    },
    {
        "name": "MycoLasso",
        "description": "MycoLasso is a Shiny app to load, visualize, and interactively explore geospatial data points.",
        "tech": ["R", "Shiny", "Leaflet"],
        "github": "https://github.com/Lucien-Piat/MycoLasso",
        "extra": ("Website", "https://lucien-piat.shinyapps.io/mycolasso/"),
        "images": ["images/mycolasso_A.png", "images/mycolasso_B.png"],
    },
    {
        "name": "Urban Tree Detection",
        "description": "Deep learning pipeline for automated tree detection and counting from satellite imagery using U-Net architecture. Developed during Erasmus+ exchange at University of Groningen.",
        "pi": "Pr Jean-Christophe Taveau",
        "tech": ["Computer Vision", "Python", "Deep Learning"],
        "extra": ("Report", "pdfs/DLF_report.pdf"),
        "images": ["images/dlf_A.png", "images/dlf_B.png"],
    },
    {
        "name": "FEAther",
        "description": "Shiny application designed for functional enrichment analysis of biological data. It allows users to upload CSV files, select various analysis options, and visualize results through interactive plots and tables.",
        "pi": "Asst. Prof Hélène Dauchel",
        "tech": ["R", "Shiny", "Functional Enrichment Analysis"],
        "github": "https://github.com/Lucien-Piat/FEAther",
        "extra": ("Website", "https://lucien-piat.shinyapps.io/feather/"),
        "images": ["images/feather_A.png", "images/feather_B.png"],
    },
    {
        "name": "Fruit Proteomics Analysis",
        "pi": "Dr Sophie Colombié",
        "description": "Statistical analysis of proteomic data across five fruit species to identify differential protein expression patterns during development. Utilized R for data processing, visualization, and interpretation.",
        "tech": ["R", "Functional Enrichment Analysis", "Proteomics"],
        "images": ["images/fruits_A.png", "images/fruits_B.png"],
    },
]

WORK_EXPERIENCE = [
    {
        "title": "Bioinformatics Engineer Intern",
        "company": "Agroscope - Wädenswil, Switzerland",
        "period": "Apr 2026 - <i>Now ⭐</i>",
        "description": "De novo genome assembly and genetic diversity analyses in Swiss ecotypes of <i>Lolium multiflorum</i>.",
    },
    {
        "title": "Bioinformatics M.Sc. Engineer Apprentice",
        "company": "INRAE BIOGECO - Cestas, France",
        "period": "2024 - 2026",
        "description": "Developing pangenomics tools and workflows to help identify structural variants in <i>Quercus spp.</i>.",
    },
    {
        "title": "Proteomics B.Sc. Research Intern",
        "company": "INRAE BFP - Villenave-d'Ornon, France",
        "period": "May - June 2023",
        "description": "Statistical analysis of fruit proteome across 5 species, identifying differential expression patterns across developmental stages.",
    },
]

EDUCATION = [
    {"degree": "M.Sc. Bioinformatics, Modeling and Statistics", "institution": "University of Rouen Normandy", "period": "2024 - 2026", "note": "2nd year of M.Sc. 18-month apprenticeship program"},
    {
        "degree": "Deep Learning Research Exchange",
        "institution": "University of Groningen - Netherlands",
        "period": "Jan - May 2024",
        "note": "Deep learning of satellite imagery applied to urban forestry",
    },
    {"degree": "M.Sc. Bioinformatics", "institution": "University of Bordeaux", "period": "2023 - 2024", "note": "1st year of M.Sc."},
    {"degree": "B.Sc. Life Sciences", "institution": "University of Bordeaux", "period": "2021 - 2023", "note": None},
]

PUBLICATIONS = [
    {
        "title": "MSpangepop: Simulating complex structural variants under advanced demographic scenarios using the coalescent",
        "authors": "L. Piat, S. Denni, S. Dubois, F. Couturier, N. Lapalu, B. Linard, C. Lemaitre, L. Duvaux",
        "venue": "JOBIM 2025, Bordeaux, France",
        "hal": "https://hal.science/hal-05219528",
    },
    {
        "title": "The pangenome of European white oaks: A new approach to identify potential barriers to gene flow",
        "authors": "F. Couturier, L. Piat, A. Mergez, F. Graziani, S. Denni, G. Magris, A. Szukala, M. Valbuena, S. Pinosio, C. Klopp, C. Rellstab, C. Plomion, E. Saez-Laguna, L. Duvaux",
        "venue": "EVOLTREE & Forgenius Final Conference, Nov 2025, Madrid, Spain",
        "hal": "https://hal.science/hal-05380966",
    },
    {
        "title": "The pangenome of European white oaks: A new approach to assess genetic diversity",
        "authors": "F. Couturier, L. Piat, S. Denni, A. Mergez, G. Magris, A. Szukala, M. Valbuena, C. Plomion, S. Pinosio, E. Saez-Laguna, C. Klopp, L. Duvaux",
        "venue": "Doctorales de la foret, Feb 2025, Poitiers, France",
        "hal": "https://hal.science/hal-05219122",
    },
]

REPORTS = [
    {
        "title": "De la construction a la simulation des pangenomes : une approche bioinformatique integree via Asm4pg et MSpangepop",
        "context": "M.Sc. apprenticeship report, INRAE BIOGECO / Univ. Rouen, 2024-2026",
        "supervisor": "Dr. Ludovic Duvaux",
        "link": "pdfs/rapport_alternance_M2_2_bims.pdf",
    },
    {
        "title": "Single Tree Detection: The Jurassic Bark",
        "context": "Erasmus+ research project, University of Groningen, March 2024",
        "authors": "M. Nurmukhambetov, C. Salzmann, K. Verhaeghe, L. Piat",
        "link": "pdfs/DLF_report.pdf",
    },
]

# Static files
STATIC_PATHS = [
    "images",
    "extras",
    "extras/CNAME",
    "extras/sitemap.xml",
    "extras/robots.txt",
    "pdfs",
]

EXTRA_PATH_METADATA = {
    "extras/CNAME": {"path": "CNAME"},
    "extras/sitemap.xml": {"path": "sitemap.xml"},
    "extras/robots.txt": {"path": "robots.txt"},
    "extras/carte_elections_bordeaux.html": {"path": "carte_elections_bordeaux.html"},
}

# Disable feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Disable unnecessary page generation
DIRECT_TEMPLATES = ["index"]
PAGINATED_TEMPLATES = {}

RELATIVE_URLS = True
