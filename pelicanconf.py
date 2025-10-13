#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Basic Information
AUTHOR = 'Lucien Piat'
SITENAME = 'Lucien Piat'
SITESUBTITLE = 'Bioinformatician | Tool and workflow development'
SITEDESCRIPTION = 'Lucien Piat - Bioinformatician | Bordeaux, France'
SITEURL = 'https://lucienpiat.fr'

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Theme
THEME = 'themes/portfolio'

# Profile
PROFILE_IMAGE = 'images/profile.jpg'
AUTHOR_EMAIL = 'lucienpiat33@gmail.com'
AUTHOR_LOCATION = 'Bordeaux, France'

# Social Links
GITHUB_URL = 'https://github.com/Lucien-Piat'
LINKEDIN_URL = 'https://www.linkedin.com/in/lucien-piat-47930419b/'


# About Section
ABOUT_ME = """
I'm a final-year <b>M2 Bioinformatics student</b> at the University of Rouen, currently completing an 18-month apprenticeship at INRAE. <br> <br>

I have experience in <b>pangenomics and genome assembly</b>, developing efficient computational solutions for large-scale genomic data analysis.
"""
# Skills Section
SKILLS = {
    'Bioinformatics': ['Genome Assembly ⋆', 'Pangenomics ⋆', 'NGS Analysis', 'Population Genetics', 
                       'Workflow Development', 'Structural Variants', 'OOP', 'Simulations'],
    'Programming': ['Python ⋆', 'Snakemake ⋆', 'Bash', 'R', 'SQL', 'Java', 'C', 'LaTeX'],
    'DevOps & HPC': ['Apptainer ⋆', 'Docker', 'SLURM', 'Git', 'Conda', 'CI/CD', 'Cluster Computing'],
}

# Projects Section
PROJECTS = [
    {
        'name': 'MSpangepop',
        'description': 'Python library for pangenome simulation under coalescent demographic models. Features clean, object-oriented architecture designed for extensibility and ease of use by biologists.',
        'tech': ['Python', 'Population Genetics', 'Coalescent Theory', 'OOP', 'MSprime / tskit', 'Pangenome Graphs'],
        'github': 'https://github.com/inrae/MSpangepop',
        'gitlab': "https://forge.inrae.fr/pangepop/MSpangepop/",
        'extra' : ("Poster", "https://lpiat-pages-cfefee.pages-forge.inrae.fr/poster_bims_lucien.pdf"),
        'images': ['images/mspangepop_A.png', 'images/mspangepop_B.png']
    },
    {
        'name': 'Asm4gp',
        'description': 'Comprehensive long-read assembly and QC pipeline supporting PacBio, ONT, TRIO, Hi-C, and HiFi data. Developed using Snakemake to automate haplotype-resolved genome assembly inputs for pangenome construction.',
        'tech': ['Snakemake', 'Python', 'SLURM', 'Apptainer', 'Conda', "Bash"],
        'github': 'https://github.com/inrae/GenomAsm4pg',
        'gitlab': 'https://forge.inrae.fr/asm4pg/GenomAsm4pg/',
        'extra' : ("Annimated flowchart", "https://asm4pg-animated-7dc863.pages-forge.inrae.fr/asm4pg_animated.html"),
        'images': ['images/asm4pg_A.png', 'images/asm4pg_B.png']
    },
    {
        'name': 'Urban Tree Detection',
        'description': 'Deep learning pipeline for automated tree detection and counting from satellite imagery using U-Net architecture. Developed during Erasmus+ exchange at University of Groningen.',
        'tech': ['Computer Vision', 'Python', 'Deep Learning'],
        'extra' : ("Report", "pdfs/DLF_report.pdf"),
        'images': ['images/dlf_A.png', 'images/dlf_B.png']
    }, 
    {
        'name': 'FEAther',
        'description': 'Shiny application designed for functional enrichment analysis of biological data. It allows users to upload CSV files, select various analysis options, and visualize results through interactive plots and tables.',
        'tech': ['R', 'Shiny', 'Functional Enrichment Analysis'],
        'github': 'https://github.com/Lucien-Piat/FEAther',
        'extra' : ("Website", "https://lucien-piat.shinyapps.io/feather/"),
        'images': ['images/feather_A.png', 'images/feather_B.png']
    },
    {
        'name': 'Fruit Proteomics Analysis',
        'description': 'Statistical analysis of proteomic data across five fruit species to identify differential protein expression patterns during development. Utilized R for data processing, visualization, and interpretation.',
        'tech': ['R', 'Functional Enrichment Analysis', 'Proteomics'],
        'images': ['images/fruits_A.png', 'images/fruits_B.png']
    }
]

WORK_EXPERIENCE = [
    {
        'title': 'Bioinformatics Engineer Apprentice',
        'company': 'INRAE BIOGECO - Cestas, France',
        'period': '2024 - 2026',
        'description': 'Developing pangenomics tools and workflows for the Pangenoak project studying structural variants in white oak genomes.'
    },
    {
        'title': 'Deep Learning Research Exchange',
        'company': 'University of Groningen - Netherlands',
        'period': 'Jan - May 2024',
        'description': 'Applied deep learning to urban forestry, building automated pipelines for tree detection from satellite imagery.'
    },
    {
        'title': 'Proteomics Research Intern',
        'company': 'INRAE BFP - Villenave-d\'Ornon, France',
        'period': 'May - June 2023',
        'description': 'Statistical analysis of fruit proteome across 5 species, identifying differential expression patterns across developmental stages.'
    },
    {
        'title': 'House Manager (Performance Nights)',
        'company': 'Bordeaux National Opera - France',
        'period': '2021 - 2025',
        'description': 'Promoted from usher to House Manager, coordinating reception teams during evening performances. Obtained SSIAP 1 fire safety certification.'
    },
]

EDUCATION = [
    {
        'degree': 'M.Sc. Bioinformatics, Modeling and Statistics',
        'institution': 'University of Rouen Normandy',
        'period': '2024 - 2026',
        'note': '18-month apprenticeship program'
    },
    {
        'degree': 'M.Sc. Bioinformatics (Year 1)',
        'institution': 'University of Bordeaux',
        'period': '2023 - 2024',
        'note': None
    },
    {
        'degree': 'B.Sc. Life Sciences',
        'institution': 'University of Bordeaux',
        'period': '2021 - 2023',
        'note': None
    }
]

ALSO = {
    'Certifications': ['SSIAP 1 (Fire Safety Certificate)', 'SST (Workplace First Aid)', "TOEIC English (970/990)"],
    'Interests': ['Hiking', 'Nature & Trees', 'Continuous Learning'],
    'Soft Skills': ['Curious', 'Quick Adaptation to New Environments', 'Team Coordination']
}

# Static files
STATIC_PATHS = [
    'images',
    'extras', 
    'extras/CNAME',
    'extras/sitemap.xml',
    'extras/robots.txt',
    "pdfs",
]
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/sitemap.xml': {'path': 'sitemap.xml'},
    'extras/robots.txt': {'path': 'robots.txt'},
}

# Disable feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Disable unnecessary page generation
DIRECT_TEMPLATES = ['index']
PAGINATED_TEMPLATES = {}

RELATIVE_URLS = True