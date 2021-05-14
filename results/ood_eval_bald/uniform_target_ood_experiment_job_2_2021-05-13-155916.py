store = {}
store['timestamp']=1620917956
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=2']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=2
store['worker_id']=2
store['num_workers']=20
store['config']={'seed': 1237, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.198180675506592})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.1555979251861572})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.2054734230041504})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.6942601203918457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.9050188064575195})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7039, 'crossentropy': 2.0665068359375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1332035064697266})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0794700384140015})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0738472938537598})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1270103454589844})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 30457], ['id', 49332], ['id', 2016], ['id', 28845], ['id', 36939], ['id', 41829], ['id', 17194], ['id', 50759], ['ood', 33528], ['id', 13517]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5242761373519897, 0.8685797452926636, 0.8373607397079468, 1.052941620349884, 0.9026563167572021, 0.6534944772720337, 0.5322032570838928, 0.5586059391498566, 0.46011388301849365, 1.1087791919708252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.7599612474441528})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.946198582649231})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.3377232551574707})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.2787814140319824})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7088, 'crossentropy': 1.52371953125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.08559250831604})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0502358675003052})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0499112606048584})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 14629], ['id', 14771], ['id', 45038], ['id', 17057], ['id', 34318], ['id', 51761], ['id', 17280], ['id', 54266], ['id', 11121], ['id', 59118]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.44201821088790894, 0.6961874961853027, 0.32692086696624756, 0.5879068374633789, 0.48507964611053467, 0.6740217208862305, 0.48682844638824463, 0.6675533652305603, 0.5225329995155334, 0.3270070552825928]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.3316395282745361})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.3488211631774902})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.531193733215332})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.477882981300354})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7811, 'crossentropy': 1.1388109375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.9434235692024231})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9387396574020386})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.8289816379547119})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 24998], ['id', 12223], ['id', 15753], ['id', 20238], ['id', 21353], ['id', 46760], ['id', 9583], ['id', 46371], ['id', 44040], ['id', 22773]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5131226181983948, 0.6924553513526917, 0.5674154162406921, 0.4589653015136719, 0.40329551696777344, 0.483978807926178, 0.6328181028366089, 0.5734885334968567, 0.560745358467102, 0.4837667942047119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1483551263809204})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.3002147674560547})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.6276490688323975})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.459763526916504})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7966, 'crossentropy': 1.07257578125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8657212257385254})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.8583686947822571})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8347266316413879})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 23927], ['id', 55509], ['id', 32276], ['id', 29438], ['id', 49199], ['id', 49586], ['id', 56049], ['id', 10390], ['id', 21304], ['id', 5662]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5164408087730408, 0.5596638917922974, 0.6326173543930054, 0.6647731065750122, 0.5691907405853271, 0.5838398933410645, 0.5678250193595886, 0.6372383236885071, 0.5422087907791138, 0.3484855890274048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0369865894317627})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.1110633611679077})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1658613681793213})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2209001779556274})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.821, 'crossentropy': 0.952969140625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8659051656723022})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7818318605422974})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7820645570755005})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 47539], ['id', 22191], ['id', 6272], ['id', 34304], ['id', 30688], ['id', 52767], ['id', 20871], ['id', 4797], ['id', 57793], ['id', 40688]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4471554756164551, 0.5165984034538269, 0.4232903718948364, 0.529915452003479, 0.4018104076385498, 0.3854635953903198, 0.38191771507263184, 0.6370356678962708, 0.46377718448638916, 0.5924744606018066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0548303127288818})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.097477912902832})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1522102355957031})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1514817476272583})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8393, 'crossentropy': 0.8749716796875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9416733980178833})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8533459901809692})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8175274729728699})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 31707], ['id', 38347], ['id', 12345], ['id', 12606], ['id', 53540], ['id', 17478], ['id', 20775], ['ood', 44000], ['id', 28958], ['ood', 57371]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.28891026973724365, 0.42841947078704834, 0.502623438835144, 0.46959710121154785, 0.3938698172569275, 0.4581754207611084, 0.48353028297424316, 0.1882857084274292, 0.5395867824554443, 0.4231031537055969]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9980369806289673})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8384295105934143})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8503005504608154})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9456499218940735})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9143247604370117})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8698, 'crossentropy': 0.71454921875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7781176567077637})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6573774814605713})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6339716911315918})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.6381450891494751})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 13049], ['id', 24124], ['id', 25704], ['id', 29905], ['id', 47068], ['id', 30844], ['ood', 44331], ['id', 29176], ['id', 24654], ['id', 39543]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4274432063102722, 0.35324472188949585, 0.21601903438568115, 0.39832770824432373, 0.4359407424926758, 0.4906168580055237, 0.23164582252502441, 0.3524794578552246, 0.4027456045150757, 0.4409630298614502]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8645111322402954})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8853793144226074})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9539016485214233})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0387707948684692})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8324, 'crossentropy': 0.814484912109375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.866868257522583})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.758918285369873})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7228693962097168})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 55623], ['id', 25886], ['id', 54472], ['id', 58845], ['id', 42878], ['id', 6280], ['id', 53549], ['id', 7631], ['id', 3762], ['id', 52661]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.271602988243103, 0.34642744064331055, 0.3790318965911865, 0.3142794966697693, 0.37483054399490356, 0.40499329566955566, 0.37659311294555664, 0.31356215476989746, 0.37217462062835693, 0.33402466773986816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9043586254119873})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7741708755493164})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7972831726074219})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8981360197067261})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9094734191894531})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8881, 'crossentropy': 0.6422712890625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8192782402038574})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.6620010137557983})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.609235942363739})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5767998099327087})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 12422], ['id', 37089], ['id', 17698], ['id', 41491], ['id', 12252], ['id', 2852], ['id', 48952], ['id', 30332], ['id', 29320], ['ood', 4194]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.35268375277519226, 0.5491905808448792, 0.4616687297821045, 0.4136934280395508, 0.26482588052749634, 0.4086175560951233, 0.4799802303314209, 0.32400643825531006, 0.42713552713394165, 0.42774128913879395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8374107480049133})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7014605402946472})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6831060647964478})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7214294672012329})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7448434233665466})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8232372999191284})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.901, 'crossentropy': 0.587737646484375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7382422685623169})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.590508222579956})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.5801293849945068})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5419172048568726})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5347869396209717})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 12581], ['ood', 43436], ['id', 53170], ['id', 1724], ['id', 57474], ['id', 9380], ['id', 49217], ['id', 54395], ['id', 25309], ['id', 37315]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.27729833126068115, 0.21311914920806885, 0.4903825521469116, 0.5486772656440735, 0.5942072868347168, 0.4914124608039856, 0.4936411380767822, 0.48814064264297485, 0.6591309309005737, 0.4927096366882324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.768683135509491})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6569874286651611})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.637526273727417})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6783930063247681})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7722142934799194})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.811930775642395})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.521527587890625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7364188432693481})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5455684661865234})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.531545877456665})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5189247131347656})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.47515106201171875})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 13428], ['id', 8299], ['id', 24408], ['id', 28154], ['id', 45073], ['id', 20120], ['ood', 9342], ['id', 43853], ['id', 27183], ['id', 16884]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5781142115592957, 0.38905763626098633, 0.40652042627334595, 0.3003438115119934, 0.49015623331069946, 0.450347363948822, 0.3485513925552368, 0.36737459897994995, 0.4860001802444458, 0.43716102838516235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8558235168457031})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6944522857666016})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7499297857284546})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7549899816513062})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.694169819355011})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8145812749862671})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.88023442029953})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0034704208374023})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.588815869140625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7751513719558716})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5400769710540771})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5310712456703186})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4676562547683716})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5026117563247681})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4927339553833008})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.43546992540359497})
store['active_learning_steps'][11]['eval_training']['best_epoch']=7
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 42020], ['id', 52688], ['id', 23584], ['id', 51298], ['id', 12399], ['id', 6874], ['id', 57290], ['id', 24533], ['id', 23400], ['id', 41088]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.554047018289566, 0.6860253214836121, 0.4648730009794235, 0.6340950131416321, 0.3317873477935791, 0.6544191837310791, 0.3578653633594513, 0.5247766971588135, 0.46565115451812744, 0.5960656404495239]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.893031120300293})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6394040584564209})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6607335805892944})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.678991436958313})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7207691669464111})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9132, 'crossentropy': 0.542073828125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7141999006271362})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6028593182563782})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5660198330879211})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5588363409042358})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 46690], ['id', 28723], ['id', 47710], ['id', 45649], ['id', 55661], ['id', 39942], ['id', 33593], ['id', 15066], ['id', 52727], ['id', 11885]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.37387949228286743, 0.5146093964576721, 0.3786812424659729, 0.35029858350753784, 0.2805885076522827, 0.2916805148124695, 0.5103623270988464, 0.32935577630996704, 0.35257065296173096, 0.5377292037010193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.826087474822998})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6811065673828125})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6138094663619995})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6655864715576172})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6609841585159302})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.767236590385437})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9181, 'crossentropy': 0.494688134765625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7002487778663635})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5363935232162476})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5077517628669739})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4949192404747009})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.49019312858581543})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 22272], ['id', 25946], ['id', 7383], ['id', 48608], ['id', 46088], ['id', 47762], ['id', 1061], ['id', 38389], ['ood', 2530], ['id', 20341]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5045389533042908, 0.3709258437156677, 0.3095349073410034, 0.4907097816467285, 0.4261918067932129, 0.4191076159477234, 0.3961198925971985, 0.3480924963951111, 0.20334601402282715, 0.274189829826355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8487392663955688})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5653285980224609})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6301789283752441})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5816589593887329})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5763250589370728})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.482605859375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.746211051940918})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.593022346496582})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5401309728622437})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48859113454818726})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 20854], ['id', 12540], ['id', 40972], ['id', 38657], ['id', 30390], ['id', 19396], ['id', 134], ['id', 23264], ['id', 18298], ['id', 19539]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4468574523925781, 0.37257814407348633, 0.32111412286758423, 0.39764076471328735, 0.368313193321228, 0.4185934066772461, 0.4037628173828125, 0.3805258274078369, 0.34550464153289795, 0.1991032361984253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8334429264068604})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6000204682350159})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5252706408500671})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.567261815071106})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6042920351028442})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6036484241485596})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.44159365234375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7503618001937866})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5419597625732422})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5479373931884766})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.49162063002586365})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5038068294525146})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 24278], ['id', 33195], ['id', 52801], ['id', 6466], ['id', 8171], ['id', 19430], ['id', 18109], ['id', 7466], ['id', 37185], ['id', 53522]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40037965774536133, 0.17431116104125977, 0.3059770464897156, 0.3752937912940979, 0.26199477910995483, 0.2622484564781189, 0.43843579292297363, 0.38114070892333984, 0.362404465675354, 0.32586246728897095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9039903879165649})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5838611125946045})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5263452529907227})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4965101480484009})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5367444753646851})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.549934983253479})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6121981143951416})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.445977978515625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7558770775794983})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5542804002761841})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4824965000152588})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.43042799830436707})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.40563201904296875})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4240504503250122})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 36550], ['id', 29347], ['ood', 59616], ['ood', 23532], ['id', 42024], ['id', 4185], ['id', 51288], ['id', 2502], ['id', 27972], ['id', 53547]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5352181792259216, 0.5230464935302734, 0.4286625385284424, 0.25347900390625, 0.3080604076385498, 0.40480172634124756, 0.3623642325401306, 0.33424943685531616, 0.4121423363685608, 0.5580389499664307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8677470684051514})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6186020374298096})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5864403247833252})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5658634901046753})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5671885013580322})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5472490787506104})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5816731452941895})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6253641843795776})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6255677938461304})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9401, 'crossentropy': 0.438871240234375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7130282521247864})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5055512189865112})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4148443937301636})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4306471347808838})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3955158591270447})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4274168908596039})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3672388195991516})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.37729549407958984})
store['active_learning_steps'][17]['eval_training']['best_epoch']=7
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 57463], ['id', 32425], ['id', 27316], ['id', 18049], ['id', 53620], ['id', 30885], ['id', 34902], ['id', 16572], ['id', 132], ['id', 39294]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.486183762550354, 0.35985416173934937, 0.41907310485839844, 0.47868216037750244, 0.4032936692237854, 0.4131154417991638, 0.39713239669799805, 0.40636157989501953, 0.29017990827560425, 0.27872318029403687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9541393518447876})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.544660210609436})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5485299825668335})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5347554683685303})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5475324392318726})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5534877777099609})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5594702959060669})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.430283837890625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8552664518356323})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5059260129928589})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4703271985054016})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4548896551132202})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.441140353679657})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.414931058883667})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 33364], ['id', 9567], ['id', 31310], ['id', 56662], ['id', 48614], ['id', 39373], ['id', 29570], ['id', 18348], ['id', 22994], ['id', 53909]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4772879481315613, 0.3678617477416992, 0.45288002490997314, 0.5374510884284973, 0.29899322986602783, 0.5068174600601196, 0.3646385669708252, 0.5690218806266785, 0.41603320837020874, 0.37038201093673706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9868779182434082})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5798310041427612})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5183038711547852})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.49855923652648926})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.494301974773407})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5376018285751343})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47100120782852173})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6407593488693237})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5201196670532227})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5096545219421387})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9441, 'crossentropy': 0.3931038330078125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8582061529159546})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5077340006828308})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4407878518104553})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3966555595397949})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.378212571144104})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3717803359031677})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37083864212036133})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35848796367645264})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3730311393737793})
store['active_learning_steps'][19]['eval_training']['best_epoch']=8
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 56773], ['id', 47680], ['id', 3030], ['ood', 12450], ['id', 6670], ['id', 158], ['id', 35152], ['id', 39762], ['id', 49841], ['ood', 3247]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3953322172164917, 0.43531298637390137, 0.41988468170166016, 0.21011602878570557, 0.3382020592689514, 0.4209598898887634, 0.459513783454895, 0.21929317712783813, 0.4029744267463684, 0.16137301921844482]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8921234607696533})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5138234496116638})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5082313418388367})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4889911413192749})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4946897327899933})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48286035656929016})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46444135904312134})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4970642626285553})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5289260745048523})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5112954378128052})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.946, 'crossentropy': 0.3723093994140625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.771449863910675})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.521565318107605})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40058326721191406})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.392686128616333})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3767855763435364})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34027987718582153})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3493767976760864})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31516194343566895})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3428814709186554})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 26358], ['id', 31850], ['id', 32730], ['id', 57914], ['id', 48512], ['id', 7305], ['id', 57324], ['id', 9428], ['id', 56454], ['id', 31535]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6616321206092834, 0.5289955735206604, 0.5001339316368103, 0.5523014664649963, 0.5160067677497864, 0.41119176149368286, 0.3299975097179413, 0.5821085572242737, 0.4063923954963684, 0.40886735916137695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9541381597518921})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5255513191223145})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4764801561832428})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4730615019798279})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5338619947433472})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4547814726829529})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48591530323028564})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.529625415802002})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4730919599533081})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.945, 'crossentropy': 0.389060400390625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7098592519760132})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5050307512283325})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.41598862409591675})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3926248848438263})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3979053199291229})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3418732285499573})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3356825113296509})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3343612551689148})
store['active_learning_steps'][21]['eval_training']['best_epoch']=8
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 34052], ['id', 53834], ['id', 33241], ['id', 36302], ['id', 6220], ['id', 59963], ['id', 55431], ['id', 34847], ['id', 55078], ['id', 41688]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5439594388008118, 0.3231704533100128, 0.3913668394088745, 0.42772746086120605, 0.44898492097854614, 0.3538799285888672, 0.27023011445999146, 0.6891076564788818, 0.4185740351676941, 0.4119876027107239]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9502401351928711})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5496492385864258})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41614437103271484})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41502922773361206})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4215618968009949})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.416744202375412})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4569520950317383})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9472, 'crossentropy': 0.3671639892578125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7831625938415527})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5114673972129822})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4284217059612274})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4542125165462494})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36847060918807983})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.35781756043434143})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 52971], ['id', 33505], ['id', 32519], ['id', 40653], ['id', 56134], ['id', 26733], ['id', 13019], ['id', 2803], ['id', 13099], ['id', 56528]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5325652360916138, 0.4475467801094055, 0.4594622254371643, 0.3550366163253784, 0.39508944749832153, 0.5970966815948486, 0.42974090576171875, 0.327300488948822, 0.34685075283050537, 0.284676730632782]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9900120496749878})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5751250982284546})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.511800229549408})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.43786686658859253})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4409196972846985})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42908143997192383})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4300665855407715})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45976054668426514})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.47059428691864014})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9471, 'crossentropy': 0.3739795166015625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8137009143829346})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.495322585105896})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38390129804611206})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3618784248828888})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37184053659439087})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.36415186524391174})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33895283937454224})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.32594960927963257})
store['active_learning_steps'][23]['eval_training']['best_epoch']=8
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 5643], ['id', 30144], ['id', 51759], ['id', 20942], ['id', 58312], ['id', 50576], ['id', 41572], ['id', 35246], ['id', 41160], ['id', 4955]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34553155303001404, 0.5683398544788361, 0.44510728120803833, 0.21558037400245667, 0.3361967206001282, 0.4895157814025879, 0.39029109477996826, 0.3453483581542969, 0.3445056676864624, 0.6156740188598633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0713979005813599})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5322044491767883})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4205101728439331})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4150353968143463})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39734119176864624})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4026668667793274})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4030824303627014})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4148872196674347})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9522, 'crossentropy': 0.3356215087890625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8530856370925903})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5260909199714661})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4288938045501709})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3968965411186218})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34929853677749634})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.364413321018219})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34451478719711304})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 8584], ['id', 8865], ['id', 18226], ['id', 21529], ['id', 7168], ['id', 43042], ['id', 29132], ['id', 33222], ['id', 59380], ['id', 36956]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.32943958044052124, 0.466489315032959, 0.39215123653411865, 0.5409572124481201, 0.4439687728881836, 0.38506019115448, 0.710013210773468, 0.3359890878200531, 0.4466904401779175, 0.37766945362091064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0011868476867676})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5181876420974731})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41006237268447876})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40702566504478455})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3834032416343689})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39008083939552307})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3876469135284424})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4003508687019348})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9524, 'crossentropy': 0.335470703125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8181965351104736})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5107391476631165})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43088918924331665})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.418937623500824})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36798936128616333})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3517034649848938})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3968697190284729})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 14484], ['id', 50417], ['id', 26444], ['id', 14697], ['id', 54916], ['id', 30897], ['id', 49576], ['id', 17540], ['id', 3094], ['id', 34587]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5668923258781433, 0.4180290102958679, 0.5772464871406555, 0.5363588929176331, 0.3569108247756958, 0.2962069511413574, 0.5115379691123962, 0.595409631729126, 0.4407097101211548, 0.318609356880188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0443438291549683})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5151789784431458})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.408439040184021})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3910776674747467})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3677465319633484})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3660739064216614})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3695560693740845})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4281349778175354})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.37551379203796387})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9566, 'crossentropy': 0.30713056640625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7943719625473022})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.48792171478271484})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39971086382865906})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3447085916996002})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.314148873090744})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3282841444015503})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3281496465206146})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29469048976898193})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 57728], ['id', 37951], ['id', 5314], ['id', 34430], ['id', 30791], ['id', 9450], ['id', 13287], ['id', 32155], ['id', 262], ['id', 5529]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5171875953674316, 0.476672887802124, 0.240523099899292, 0.43484604358673096, 0.2771676331758499, 0.4000852704048157, 0.5117305517196655, 0.6076264977455139, 0.2643011808395386, 0.6770199835300446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9525324702262878})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6505886316299438})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4360508620738983})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.42982444167137146})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3982856273651123})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.38966792821884155})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42906245589256287})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4150583744049072})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4375770092010498})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.33558876953125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8379992842674255})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.51166832447052})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41493403911590576})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3581978678703308})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3284873366355896})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.331550657749176})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35280662775039673})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32100439071655273})
store['active_learning_steps'][27]['eval_training']['best_epoch']=8
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 34578], ['id', 40066], ['id', 49517], ['ood', 40052], ['id', 4205], ['id', 24145], ['id', 19837], ['id', 2231], ['id', 46110], ['id', 25246]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3656955361366272, 0.5451654195785522, 0.6326261758804321, 0.27528274059295654, 0.4765121340751648, 0.5174042582511902, 0.5416762828826904, 0.5028327703475952, 0.2779109477996826, 0.4975236654281616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0440692901611328})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5849420428276062})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41377711296081543})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.40811681747436523})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37819069623947144})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4316670298576355})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40915346145629883})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4100463390350342})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9533, 'crossentropy': 0.316294873046875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8613134622573853})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4838602542877197})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41563481092453003})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35368961095809937})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3719245195388794})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35371261835098267})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3630991578102112})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42472], ['id', 44927], ['id', 46530], ['id', 15739], ['id', 34485], ['id', 10873], ['id', 21396], ['id', 45212], ['id', 11613], ['id', 46283]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4375596046447754, 0.4468621611595154, 0.2729809880256653, 0.4425770044326782, 0.4932977706193924, 0.4994843602180481, 0.4224540889263153, 0.23701101541519165, 0.27622443437576294, 0.3132941797375679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.02297043800354})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48686352372169495})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3629818558692932})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3466908037662506})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32792240381240845})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3408225178718567})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3377716541290283})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34538206458091736})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.28410498046875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9083458781242371})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.48983389139175415})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.408541738986969})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.365904301404953})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38755011558532715})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3626447319984436})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3500140905380249})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 36298], ['id', 49021], ['ood', 43952], ['id', 4058], ['id', 31413], ['ood', 45579], ['ood', 46547], ['id', 7498], ['id', 8458], ['ood', 18798]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3342357873916626, 0.3848576545715332, 0.5064362287521362, 0.5214986205101013, 0.38796520233154297, 0.21497809886932373, 0.39478421211242676, 0.3865201473236084, 0.31652402877807617, 0.23773610591888428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9650444388389587})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5171274542808533})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.44458603858947754})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3312874436378479})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3306778073310852})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3120120167732239})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3746083378791809})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3429926037788391})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37097102403640747})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9613, 'crossentropy': 0.2784825439453125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8563830852508545})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49342599511146545})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4300745129585266})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3914050757884979})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35635170340538025})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3246094584465027})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30593663454055786})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30239632725715637})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 39891], ['id', 49541], ['id', 6524], ['id', 49511], ['id', 234], ['id', 59294], ['id', 2595], ['id', 40469], ['id', 59783], ['id', 42096]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5125727653503418, 0.618690013885498, 0.43354684114456177, 0.4615088701248169, 0.37247681617736816, 0.3693341016769409, 0.3862505257129669, 0.33014267683029175, 0.5013837814331055, 0.45494383573532104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0286343097686768})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5054934024810791})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4322894811630249})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3722129464149475})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3559613823890686})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3557559549808502})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39971762895584106})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3484352231025696})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34902021288871765})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35726702213287354})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3458535373210907})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3488805294036865})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3841996192932129})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4046022593975067})
store['active_learning_steps'][31]['training']['best_epoch']=11
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.3229285400390625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8209872841835022})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47964221239089966})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38780587911605835})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34558600187301636})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29523617029190063})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28917425870895386})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.279194176197052})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2645281255245209})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2635505795478821})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2675519287586212})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2848989963531494})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25097236037254333})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.268310010433197})
store['active_learning_steps'][31]['eval_training']['best_epoch']=12
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 6304], ['id', 9294], ['id', 17216], ['id', 16198], ['ood', 15938], ['id', 9687], ['id', 34761], ['id', 37383], ['id', 22193], ['id', 39778]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.505232036113739, 0.5226477384567261, 0.396881103515625, 0.6293998062610626, 0.338645339012146, 0.6110253930091858, 0.4469151198863983, 0.32183581590652466, 0.4990978240966797, 0.7200241088867188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0878127813339233})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.539695680141449})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45183244347572327})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3801725506782532})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3637169599533081})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37101757526397705})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3504493832588196})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3787110447883606})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3700721859931946})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3791859745979309})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9579, 'crossentropy': 0.2962620849609375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8603919744491577})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4936619997024536})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.413774311542511})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33601078391075134})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34746676683425903})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3444952070713043})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3065829277038574})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3124205768108368})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31504958868026733})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 7833], ['id', 7768], ['id', 49088], ['id', 18951], ['id', 47845], ['id', 15261], ['id', 27065], ['id', 19454], ['id', 26336], ['id', 57342]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44712406396865845, 0.4667815566062927, 0.335795521736145, 0.3234986662864685, 0.3536137342453003, 0.40932905673980713, 0.6748239994049072, 0.3466956913471222, 0.2718127369880676, 0.594898521900177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9804171323776245})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5129108428955078})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40372273325920105})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3686993420124054})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34368109703063965})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3656267523765564})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31975287199020386})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35099923610687256})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3439350724220276})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34453827142715454})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.2631303466796875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.941503643989563})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4823986291885376})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38373926281929016})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.337682843208313})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28367218375205994})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30202409625053406})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27975812554359436})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3212851881980896})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2892889380455017})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 27172], ['id', 41751], ['id', 14650], ['id', 54195], ['id', 53872], ['id', 14896], ['id', 51180], ['id', 57742], ['id', 24630], ['id', 53906]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4789050817489624, 0.28566601872444153, 0.3627052903175354, 0.6430531442165375, 0.4772927761077881, 0.3637004494667053, 0.5298723578453064, 0.2972882390022278, 0.25141167640686035, 0.4178818464279175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1428451538085938})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6520662307739258})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4670141935348511})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3926478922367096})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34911590814590454})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3605716824531555})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3297748565673828})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3426675796508789})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33863046765327454})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32345613837242126})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35868343710899353})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35682690143585205})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40621331334114075})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9634, 'crossentropy': 0.2860575439453125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8909691572189331})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5172745585441589})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3787009119987488})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3152974545955658})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33660584688186646})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30749034881591797})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2904895842075348})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3088386654853821})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2750835418701172})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26140785217285156})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28675684332847595})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2720106244087219})
store['active_learning_steps'][34]['eval_training']['best_epoch']=10
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 42886], ['id', 34406], ['id', 26760], ['id', 24805], ['id', 11621], ['id', 22590], ['id', 56636], ['id', 45005], ['id', 56588], ['id', 38276]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3965679407119751, 0.4079248309135437, 0.41863954067230225, 0.42072439193725586, 0.45138829946517944, 0.4552766680717468, 0.35996878147125244, 0.35558730363845825, 0.4534339904785156, 0.47859716415405273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.063575267791748})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5537475347518921})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39599278569221497})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3567036986351013})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.299897164106369})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30789855122566223})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28462859988212585})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3009732961654663})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34027618169784546})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3053337335586548})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9651, 'crossentropy': 0.2521795654296875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8650343418121338})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4937261939048767})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3634181022644043})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.346890926361084})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2992163896560669})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2874135673046112})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2711666524410248})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28523802757263184})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30662012100219727})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 16084], ['id', 28930], ['id', 31591], ['id', 24263], ['id', 21598], ['id', 50827], ['id', 21601], ['id', 23886], ['id', 23868], ['id', 34934]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.32387906312942505, 0.38344067335128784, 0.3117855191230774, 0.5505697727203369, 0.3527171015739441, 0.37106865644454956, 0.5017035007476807, 0.5177640914916992, 0.2235691249370575, 0.37258607149124146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0057213306427002})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5733906030654907})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44302093982696533})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.364982932806015})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34299349784851074})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3876435160636902})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31711453199386597})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3442964255809784})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33658888936042786})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34405815601348877})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.27358349609375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9401326179504395})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47717052698135376})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42013221979141235})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.356831431388855})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32824069261550903})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.314327597618103})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3011247515678406})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3162856101989746})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3168049454689026})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 22139], ['id', 39126], ['id', 51263], ['id', 52744], ['id', 28340], ['id', 59314], ['id', 6980], ['id', 43796], ['id', 39940], ['id', 14825]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5396673083305359, 0.4437308609485626, 0.3570363521575928, 0.4770100712776184, 0.39474087953567505, 0.46454644203186035, 0.5670189261436462, 0.5534691214561462, 0.35651895403862, 0.49766361713409424]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1416484117507935})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5889641046524048})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43890783190727234})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34047627449035645})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3415311872959137})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3003975450992584})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3243699073791504})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3231431841850281})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3474763035774231})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.2775906982421875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9318723678588867})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5269935131072998})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39898425340652466})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3627292513847351})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35646671056747437})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3444511890411377})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31837475299835205})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31081175804138184})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 49844], ['id', 29839], ['id', 13876], ['id', 55532], ['id', 45787], ['id', 19542], ['id', 13075], ['id', 57018], ['id', 39672], ['id', 43262]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.32117199897766113, 0.37909138202667236, 0.40265870094299316, 0.3604133725166321, 0.33871030807495117, 0.3670034408569336, 0.27484381198883057, 0.38934457302093506, 0.2970283031463623, 0.4071633815765381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1690293550491333})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5491344332695007})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3682340383529663})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37668681144714355})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3079921007156372})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.304500013589859})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3088446259498596})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28447020053863525})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2973420023918152})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3193652033805847})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31881171464920044})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.256824365234375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7883345484733582})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5284204483032227})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3800167441368103})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3302539587020874})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3185559809207916})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2844405174255371})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2834791839122772})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2603050470352173})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2575615644454956})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2781327962875366})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 49892], ['id', 29530], ['id', 52978], ['id', 29431], ['id', 44091], ['id', 54878], ['id', 22155], ['id', 48504], ['id', 42140], ['id', 29142]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.41322213411331177, 0.5173359513282776, 0.46040499210357666, 0.4111694395542145, 0.44143229722976685, 0.4290536046028137, 0.34434187412261963, 0.4692591428756714, 0.365012526512146, 0.39506351947784424]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1150238513946533})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5273680090904236})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4314091205596924})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34219300746917725})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3371644616127014})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3176969289779663})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3107982873916626})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30584776401519775})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3288519084453583})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3150596022605896})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2970482110977173})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30676472187042236})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31102293729782104})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3030898869037628})
store['active_learning_steps'][39]['training']['best_epoch']=11
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.2576309326171875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8889256715774536})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5314797759056091})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3949993848800659})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3571363091468811})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31192415952682495})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2850490212440491})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26820749044418335})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25962603092193604})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27196604013442993})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23604947328567505})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24861761927604675})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23488380014896393})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.22081217169761658})
store['active_learning_steps'][39]['eval_training']['best_epoch']=13
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 40022], ['id', 49890], ['id', 52800], ['id', 3719], ['id', 8719], ['id', 36450], ['id', 54880], ['id', 54520], ['id', 39764], ['id', 38210]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5162758231163025, 0.6509989500045776, 0.4042433500289917, 0.6023227572441101, 0.49008214473724365, 0.3818622827529907, 0.7245035767555237, 0.4418489933013916, 0.6570940017700195, 0.32106029987335205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1253567934036255})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5517637729644775})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4146993160247803})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34146633744239807})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.301891028881073})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29771658778190613})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.335974782705307})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27989649772644043})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29434552788734436})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2848232090473175})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3058243691921234})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.2517852783203125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9352526664733887})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4883740544319153})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3939679265022278})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3253365159034729})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2836586833000183})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31300365924835205})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30384618043899536})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28773626685142517})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 8449], ['id', 48762], ['id', 26613], ['id', 20072], ['id', 32829], ['id', 24360], ['id', 9396], ['id', 13074], ['id', 28102], ['id', 50162]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.25869280099868774, 0.4459335207939148, 0.36637306213378906, 0.4672672748565674, 0.43716931343078613, 0.5346198678016663, 0.3897157311439514, 0.41290998458862305, 0.6377346515655518, 0.44710856676101685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.143854022026062})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6661486625671387})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4363967776298523})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3461062014102936})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28684985637664795})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3049558401107788})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29299411177635193})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2836017608642578})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2694379389286041})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2908638119697571})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2921217679977417})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28003761172294617})
store['active_learning_steps'][41]['training']['best_epoch']=9
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.24843564453125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.995545506477356})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5378819704055786})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4234919548034668})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3511704206466675})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31405162811279297})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29916203022003174})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2952269911766052})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28476980328559875})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28686660528182983})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2738751471042633})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25677937269210815})
store['active_learning_steps'][41]['eval_training']['best_epoch']=11
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 17282], ['id', 41054], ['id', 7678], ['id', 33552], ['id', 11797], ['id', 31302], ['id', 55116], ['id', 16031], ['id', 1870], ['id', 56621]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5504835844039917, 0.4890798330307007, 0.6077802181243896, 0.45136797428131104, 0.5513948202133179, 0.5421570539474487, 0.5781057476997375, 0.5105356574058533, 0.5426779389381409, 0.6113273501396179]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2262052297592163})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5608360171318054})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4529210925102234})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.316669762134552})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.275922566652298})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3056308925151825})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26005733013153076})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25935518741607666})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2967014014720917})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3006691336631775})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2721348702907562})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.256671484375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9275379180908203})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5531628131866455})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4245172142982483})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32598137855529785})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2718994915485382})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2889559864997864})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2873060703277588})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25544679164886475})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.271010160446167})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26628047227859497})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 21128], ['id', 17509], ['id', 13259], ['id', 4694], ['id', 23546], ['id', 31579], ['id', 52294], ['id', 14687], ['id', 26293], ['id', 21372]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2523018717765808, 0.4381290376186371, 0.43756479024887085, 0.4815022945404053, 0.32671433687210083, 0.4484531581401825, 0.45026695728302, 0.378343403339386, 0.4227985143661499, 0.47683900594711304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1213085651397705})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5326688289642334})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38707852363586426})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.323813796043396})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30249208211898804})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27690359950065613})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24698668718338013})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2578057646751404})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2501794695854187})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26360273361206055})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.245385009765625}
