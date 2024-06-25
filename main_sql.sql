SELECT
    p.ID,
    p.post_title,
    post_date,
    p.tct_update_date as 'update_date',
    concat('theculturetrip.com', l.url,'articles/',p.post_name) as 'URL',
    (SELECT t.`name`
        FROM wp_terms as t
            LEFT JOIN wp_term_taxonomy AS tt on t.term_id = tt.term_id
            LEFT JOIN wp_term_relationships AS tr on tt.term_taxonomy_id = tr.term_taxonomy_id
        WHERE t.term_id = tt.term_id AND tt.taxonomy = 'category' AND p.ID = tr.object_id) AS 'Genre',
    (SELECT t.`name`
        FROM wp_article_categories as t
            LEFT JOIN wp_article_categories_relationships AS tt on t.id = tt.category_id
        WHERE p.ID = tt.article_id) AS 'Category',
    l.slug as 'Country',
    l.url as 'Location',
    p.post_name
FROM
    thecurturetrip.wp_posts as p
        left join wp_postmeta as m on p.ID = m.post_id
        left join guides_location_cache as l on m.meta_value = l.kgid
WHERE
    p.post_status = 'publish' and
    p.post_type = 'article' and
    m.meta_key = 'kg_id' and
    p.post_name REGEXP '%2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021|2022|2023|2024%'
ORDER BY
    p.tct_update_date DESC

select *
from wp_posts
where
    post_status = 'publish'
    and post_type = 'article'
    and post_name REGEXP '%2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021|2022|2023|2024%'


SELECT
    p.ID,
    p.post_title,
    post_date,
    p.tct_update_date as 'update_date',
    p.post_modified as 'modified_date',
    concat('theculturetrip.com', l.url,'articles/',p.post_name) as 'URL',
    (SELECT t.`name`
     FROM wp_terms as t
              LEFT JOIN wp_term_taxonomy AS tt on t.term_id = tt.term_id
              LEFT JOIN wp_term_relationships AS tr on tt.term_taxonomy_id = tr.term_taxonomy_id
     WHERE t.term_id = tt.term_id AND tt.taxonomy = 'category' AND p.ID = tr.object_id) AS 'Genre',
    (SELECT t.`name`
     FROM wp_article_categories as t
              LEFT JOIN wp_article_categories_relationships AS tt on t.id = tt.category_id
     WHERE p.ID = tt.article_id) AS 'Category',
    l.slug as 'Country',
    l.url as 'Location',
    p.post_name
FROM
    thecurturetrip.wp_posts as p
        left join wp_postmeta as m on p.ID = m.post_id
        left join guides_location_cache as l on m.meta_value = l.kgid
WHERE
        p.post_status = 'publish' and
        p.post_type = 'article' and
        m.meta_key = 'kg_id' and
        p.post_modified > '2024-01-01'
ORDER BY
    p.post_modified DESC;