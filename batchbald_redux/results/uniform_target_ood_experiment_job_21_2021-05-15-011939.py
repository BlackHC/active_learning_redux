store = {}
store['timestamp']=1621037979
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=21']
store['commit']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['github_url']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=21
store['worker_id']=21
store['num_workers']=30
store['config']={'seed': 1262, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.EvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset: FastMNIST (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.416628837585449})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.129458427429199})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.6179609298706055})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.5014255046844482})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6026, 'crossentropy': 2.453809375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3287221193313599})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.335662841796875})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2829062938690186})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 42566], ['ood', 7328], ['ood', 37112], ['ood', 45148], ['ood', 45173], ['ood', 43832], ['ood', 30311], ['ood', 22652], ['ood', 43634], ['ood', 56094]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.1000584363937378, 1.0893035531044006, 1.0742629766464233, 1.0620577335357666, 1.040389358997345, 1.0383283495903015, 1.034460961818695, 1.0327343940734863, 1.0313410758972168, 1.0230093002319336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 2.158977508544922})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.8838934898376465})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.30631685256958})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.3421127796173096})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5648, 'crossentropy': 2.2635111328125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.3521270751953125})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3969342708587646})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.3200925588607788})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 15335], ['id', 57864], ['id', 35445], ['id', 57139], ['id', 28336], ['id', 11182], ['id', 35356], ['id', 11226], ['id', 48722], ['id', 12019]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7903510332107544, 0.7882308959960938, 0.776130735874176, 0.769071638584137, 0.766934871673584, 0.7643224596977234, 0.7559945583343506, 0.7541711330413818, 0.7534308433532715, 0.7520513534545898]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 2.3002209663391113})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 3.24910831451416})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 3.596531391143799})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 4.09211540222168})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5354, 'crossentropy': 2.3551298828125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 1.45065438747406})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.448394775390625})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.4604216814041138})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 24858], ['id', 59884], ['id', 36013], ['id', 13116], ['id', 48000], ['id', 47728], ['id', 1180], ['id', 54957], ['id', 42916], ['id', 1214]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5569571256637573, 0.5452173948287964, 0.5328328013420105, 0.5296237468719482, 0.5196678042411804, 0.518164336681366, 0.5168017745018005, 0.5158584117889404, 0.514450192451477, 0.5124225616455078]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5341796875, 'crossentropy': 1.8548709154129028})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.5237598419189453})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 2.863799810409546})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.319333791732788})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5327, 'crossentropy': 1.960721875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5419921875, 'crossentropy': 1.4404022693634033})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.55078125, 'crossentropy': 1.3638668060302734})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.4270585775375366})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 25993], ['ood', 28391], ['ood', 16945], ['ood', 28409], ['ood', 28515], ['ood', 38827], ['ood', 8700], ['ood', 10319], ['ood', 27917], ['ood', 15246]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5987789630889893, 0.5550233721733093, 0.5447020530700684, 0.5442245006561279, 0.5441999435424805, 0.5394147634506226, 0.5386238098144531, 0.5372462272644043, 0.5312907695770264, 0.5309967994689941]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.7421518564224243})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 2.27923583984375})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.935762405395508})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.397413730621338})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5174, 'crossentropy': 1.83197734375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.5217610597610474})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.537109375, 'crossentropy': 1.4640096426010132})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.448216438293457})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 15929], ['id', 1191], ['id', 8321], ['id', 54167], ['id', 45121], ['id', 36985], ['id', 33663], ['id', 42521], ['id', 15208], ['id', 52428]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5485893487930298, 0.5374531745910645, 0.5335856080055237, 0.532914400100708, 0.5294663906097412, 0.5278403162956238, 0.5253373384475708, 0.5251566171646118, 0.5248678922653198, 0.5227652788162231]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.608549952507019})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 2.0528671741485596})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 2.6635050773620605})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 3.1361823081970215})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5064, 'crossentropy': 1.7240857421875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.4736328125, 'crossentropy': 1.5021870136260986})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.4921875, 'crossentropy': 1.4657262563705444})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.4775390625, 'crossentropy': 1.479274868965149})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 36884], ['id', 51447], ['id', 28830], ['id', 26960], ['id', 42778], ['id', 24622], ['id', 46845], ['id', 7156], ['id', 12326], ['id', 54433]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3146727681159973, 0.31110459566116333, 0.3084350824356079, 0.304928183555603, 0.3047395348548889, 0.30458664894104004, 0.3033548593521118, 0.301794171333313, 0.3009617328643799, 0.3005080223083496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.7883654832839966})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 2.3935136795043945})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.6045947074890137})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 3.2053256034851074})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.4896, 'crossentropy': 1.822569921875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.423828125, 'crossentropy': 1.6559549570083618})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.4453125, 'crossentropy': 1.6075387001037598})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.46484375, 'crossentropy': 1.6076147556304932})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 39959], ['id', 360], ['id', 26781], ['id', 2574], ['id', 33534], ['id', 59763], ['id', 52550], ['id', 26246], ['id', 19521], ['id', 53357]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.38809096813201904, 0.3812168836593628, 0.37998831272125244, 0.36946821212768555, 0.3692684769630432, 0.368647038936615, 0.3658396005630493, 0.36381351947784424, 0.3636210560798645, 0.36344456672668457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.439453125, 'crossentropy': 1.7149286270141602})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.8255376815795898})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 2.689119338989258})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 2.6591453552246094})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.4258, 'crossentropy': 1.7764361328125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.4013671875, 'crossentropy': 1.6857600212097168})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.4267578125, 'crossentropy': 1.5947637557983398})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.4169921875, 'crossentropy': 1.6389524936676025})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 6008], ['id', 59894], ['id', 27739], ['id', 15377], ['id', 7671], ['id', 1893], ['id', 32396], ['id', 35832], ['id', 2445], ['id', 51919]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.267744243144989, 0.267037034034729, 0.2654458284378052, 0.2652989625930786, 0.2614644467830658, 0.2610257863998413, 0.25943446159362793, 0.25915825366973877, 0.25837957859039307, 0.25796598196029663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.490234375, 'crossentropy': 1.5793488025665283})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.5924402475357056})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.0168895721435547})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.14833664894104})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.4864, 'crossentropy': 1.6034701171875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.4296875, 'crossentropy': 1.6398662328720093})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.431640625, 'crossentropy': 1.5703109502792358})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.4287109375, 'crossentropy': 1.5867606401443481})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 45967], ['id', 41210], ['id', 58708], ['id', 47088], ['id', 43015], ['id', 46601], ['id', 29580], ['id', 44063], ['id', 7842], ['id', 25803]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3006404638290405, 0.29891860485076904, 0.2764859199523926, 0.27242302894592285, 0.26925426721572876, 0.2672901153564453, 0.2670491933822632, 0.2663387060165405, 0.2628527879714966, 0.2628523111343384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.505859375, 'crossentropy': 1.6184544563293457})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.55078125, 'crossentropy': 1.7335853576660156})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.1684420108795166})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.2189645767211914})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.4607, 'crossentropy': 1.634626171875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.4052734375, 'crossentropy': 1.6791622638702393})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.4169921875, 'crossentropy': 1.5884013175964355})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.4150390625, 'crossentropy': 1.586593508720398})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 11769], ['ood', 31255], ['ood', 40775], ['ood', 10211], ['ood', 8797], ['ood', 8817], ['ood', 11803], ['ood', 11819], ['ood', 9997], ['ood', 20781]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3049267530441284, 0.2992011308670044, 0.29770100116729736, 0.2962852716445923, 0.2961106300354004, 0.295975923538208, 0.29209816455841064, 0.291942834854126, 0.2903329133987427, 0.28959405422210693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.443359375, 'crossentropy': 1.6562570333480835})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.4824795722961426})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.7003614902496338})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.149285316467285})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.2683768272399902})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5707, 'crossentropy': 1.51420986328125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.3843402862548828})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.55078125, 'crossentropy': 1.350433349609375})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.343946933746338})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.3266178369522095})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 326], ['id', 56948], ['id', 628], ['id', 24312], ['id', 45116], ['id', 30784], ['id', 42560], ['id', 9943], ['id', 47079], ['id', 13183]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4625375270843506, 0.4508627653121948, 0.4255077838897705, 0.4137364625930786, 0.4109008312225342, 0.40793609619140625, 0.40587544441223145, 0.3954947590827942, 0.3949763774871826, 0.39218413829803467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.4296875, 'crossentropy': 1.6152490377426147})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.538740634918213})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.8416037559509277})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.9653115272521973})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.116412878036499})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.563, 'crossentropy': 1.58464169921875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.4159693717956543})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5546875, 'crossentropy': 1.3593971729278564})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.335033893585205})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3269741535186768})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 21615], ['id', 34620], ['ood', 46892], ['ood', 40082], ['ood', 50630], ['ood', 48877], ['ood', 53298], ['ood', 43610], ['ood', 3370], ['ood', 21890]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5458892583847046, 0.5286170244216919, 0.5097339749336243, 0.508691132068634, 0.5047440528869629, 0.5044496059417725, 0.5029422044754028, 0.5020192861557007, 0.501750111579895, 0.4932992458343506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.521484375, 'crossentropy': 1.5636173486709595})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.5175673961639404})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.9681706428527832})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.9712862968444824})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.206056594848633})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5816, 'crossentropy': 1.51802724609375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.51171875, 'crossentropy': 1.4636707305908203})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.3308477401733398})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.306416392326355})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.310523271560669})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 12617], ['id', 12302], ['id', 26518], ['id', 16210], ['id', 32672], ['id', 48647], ['id', 2089], ['id', 55392], ['id', 49078], ['id', 38156]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3311002850532532, 0.3300771713256836, 0.32773149013519287, 0.32520508766174316, 0.32351791858673096, 0.32019615173339844, 0.3201412558555603, 0.31564295291900635, 0.3154369592666626, 0.3147096633911133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.494140625, 'crossentropy': 1.5772507190704346})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.4215099811553955})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.6270546913146973})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.7518205642700195})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.1430962085723877})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5754, 'crossentropy': 1.41531708984375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.515625, 'crossentropy': 1.448781967163086})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5341796875, 'crossentropy': 1.3233036994934082})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.2622177600860596})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.2852277755737305})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 59771], ['id', 14065], ['id', 49891], ['id', 6572], ['id', 21901], ['id', 26219], ['id', 24172], ['id', 56561], ['id', 54778], ['id', 46307]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3593747019767761, 0.35163044929504395, 0.3494158983230591, 0.34475529193878174, 0.3324868083000183, 0.331295371055603, 0.3282272219657898, 0.32814735174179077, 0.32741880416870117, 0.3259871006011963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.4990234375, 'crossentropy': 1.4816844463348389})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.2797268629074097})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.5088703632354736})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.5970162153244019})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.7874770164489746})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.594, 'crossentropy': 1.2958837890625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5341796875, 'crossentropy': 1.3504374027252197})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.2436633110046387})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.2475166320800781})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.187276005744934})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 22288], ['id', 4195], ['id', 3540], ['id', 46064], ['id', 43277], ['id', 50369], ['id', 54405], ['id', 34750], ['id', 25184], ['id', 38307]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3308044672012329, 0.3292093276977539, 0.31939518451690674, 0.3025493621826172, 0.29946577548980713, 0.29385650157928467, 0.29245924949645996, 0.29045939445495605, 0.2900865077972412, 0.2896479368209839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.4970703125, 'crossentropy': 1.5495023727416992})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.3797235488891602})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.428729772567749})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.6448709964752197})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.8612420558929443})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5708, 'crossentropy': 1.4412537109375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.3892440795898438})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.3245127201080322})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.265749454498291})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.30013108253479})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 4752], ['id', 57504], ['id', 27409], ['id', 40304], ['id', 54813], ['id', 38886], ['id', 43265], ['id', 45740], ['id', 57944], ['id', 27090]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.38256359100341797, 0.38103675842285156, 0.36107051372528076, 0.36071574687957764, 0.35387253761291504, 0.34661412239074707, 0.344693660736084, 0.34061479568481445, 0.3394533395767212, 0.33668649196624756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.484375, 'crossentropy': 1.5744041204452515})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.347853422164917})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3696061372756958})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.7293978929519653})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.636051893234253})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.5651, 'crossentropy': 1.38384140625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.513671875, 'crossentropy': 1.4335495233535767})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.3294498920440674})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.3111729621887207})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.3024474382400513})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 12078], ['id', 14667], ['id', 11473], ['id', 34920], ['id', 9650], ['id', 22547], ['id', 23684], ['id', 33673], ['id', 27800], ['id', 10406]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3058590888977051, 0.28203320503234863, 0.28152966499328613, 0.27853381633758545, 0.2768596410751343, 0.2737542390823364, 0.27305328845977783, 0.26824307441711426, 0.26741325855255127, 0.26572465896606445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.4697265625, 'crossentropy': 1.6462428569793701})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.4674373865127563})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.376512050628662})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.5790950059890747})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.8746498823165894})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.7737064361572266})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.5758, 'crossentropy': 1.47569453125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5078125, 'crossentropy': 1.3934427499771118})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.3149588108062744})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.297451138496399})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.2763538360595703})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.2653629779815674})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 55157], ['id', 39750], ['id', 39707], ['id', 43193], ['id', 57751], ['id', 33166], ['id', 37501], ['id', 51328], ['id', 19100], ['id', 31698]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3872877359390259, 0.3771461844444275, 0.3690471351146698, 0.3602449893951416, 0.35938525199890137, 0.35828447341918945, 0.3557294011116028, 0.3550163507461548, 0.3543339967727661, 0.3524515628814697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.45703125, 'crossentropy': 1.5687808990478516})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 1.341791033744812})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.448223352432251})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.536813735961914})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.6606156826019287})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.532, 'crossentropy': 1.41566767578125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.4814453125, 'crossentropy': 1.450727939605713})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.3534598350524902})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.3373076915740967})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.336961030960083})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 13598], ['id', 31662], ['id', 52509], ['id', 30476], ['id', 57000], ['id', 2181], ['id', 55098], ['id', 3913], ['id', 42587], ['id', 33674]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3565024137496948, 0.339280366897583, 0.32264864444732666, 0.31596195697784424, 0.30081164836883545, 0.2991863489151001, 0.29885876178741455, 0.29703211784362793, 0.28782665729522705, 0.2874753475189209]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.451171875, 'crossentropy': 1.6659836769104004})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5029296875, 'crossentropy': 1.4921536445617676})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.5103607177734375})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4074938297271729})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.4610669612884521})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.9413328170776367})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.8861666917800903})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.5969, 'crossentropy': 1.47688056640625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.5263671875, 'crossentropy': 1.390822410583496})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.308596134185791})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.2289851903915405})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1981556415557861})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2128798961639404})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1816123723983765})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 27372], ['id', 38100], ['id', 11901], ['id', 530], ['id', 16767], ['id', 57620], ['id', 5692], ['id', 15841], ['id', 31587], ['id', 26258]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45140671730041504, 0.44351309537887573, 0.43070709705352783, 0.42578279972076416, 0.4163680672645569, 0.4134060740470886, 0.4087793827056885, 0.4051046371459961, 0.4012855291366577, 0.39185500144958496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.4326171875, 'crossentropy': 1.6542110443115234})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.462890625, 'crossentropy': 1.5097354650497437})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.401757001876831})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.5554311275482178})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.4463694095611572})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.5574979782104492})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.5675, 'crossentropy': 1.4357861328125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.5078125, 'crossentropy': 1.4336719512939453})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.2741312980651855})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.250549077987671})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 1.252382516860962})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.206062912940979})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 55765], ['id', 12467], ['id', 58130], ['id', 13454], ['id', 21404], ['id', 26217], ['id', 49008], ['id', 23414], ['id', 17046], ['id', 28159]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4412119388580322, 0.43699777126312256, 0.42041754722595215, 0.41537928581237793, 0.40426385402679443, 0.4033287763595581, 0.4016287326812744, 0.4016059637069702, 0.3943455219268799, 0.3926064968109131]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.4765625, 'crossentropy': 1.610609769821167})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.3792839050292969})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.394040822982788})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3680288791656494})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.3874834775924683})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.5922709703445435})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.7935171127319336})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6198, 'crossentropy': 1.39319052734375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.3257243633270264})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.1969375610351562})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.1678690910339355})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.147761344909668})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.1506125926971436})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1156303882598877})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 48595], ['id', 26254], ['id', 47989], ['id', 33875], ['id', 32778], ['id', 6424], ['id', 32982], ['id', 3895], ['id', 4267], ['id', 4618]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5193504095077515, 0.4725114107131958, 0.4643259048461914, 0.46382319927215576, 0.4488241672515869, 0.43771862983703613, 0.4366123676300049, 0.43166041374206543, 0.4310716390609741, 0.4252910614013672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.462890625, 'crossentropy': 1.6265690326690674})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.4755332469940186})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.57028067111969})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.5189214944839478})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.6423624753952026})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.5495, 'crossentropy': 1.51753193359375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.4921875, 'crossentropy': 1.4646008014678955})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.5146484375, 'crossentropy': 1.427673101425171})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.51953125, 'crossentropy': 1.4193882942199707})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.5185546875, 'crossentropy': 1.3855795860290527})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 52778], ['id', 22163], ['ood', 53172], ['id', 4123], ['id', 57520], ['id', 32338], ['ood', 22037], ['id', 19378], ['ood', 22057], ['id', 17950]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.30573463439941406, 0.30556607246398926, 0.2936810255050659, 0.29256367683410645, 0.2868530750274658, 0.2853388786315918, 0.285114049911499, 0.28347039222717285, 0.2831146717071533, 0.28055059909820557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.4697265625, 'crossentropy': 1.5639054775238037})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.3941552639007568})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2520793676376343})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3630931377410889})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2911373376846313})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3847851753234863})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6324, 'crossentropy': 1.31303642578125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.3172439336776733})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.2043949365615845})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1787738800048828})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.171220064163208})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1514211893081665})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 55968], ['id', 70], ['id', 20366], ['id', 59100], ['id', 11702], ['id', 15525], ['id', 27863], ['id', 40242], ['id', 45262], ['id', 25070]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4763352870941162, 0.4547858238220215, 0.44761979579925537, 0.42478835582733154, 0.42474865913391113, 0.4071016311645508, 0.4052685499191284, 0.4007833003997803, 0.4002370834350586, 0.3981431722640991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.4814453125, 'crossentropy': 1.578122615814209})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.2591568231582642})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2151566743850708})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.306386947631836})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.362553596496582})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4204254150390625})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6295, 'crossentropy': 1.25628525390625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.251273512840271})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.1628525257110596})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.117287516593933})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.1089282035827637})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.0913805961608887})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 57297], ['id', 25963], ['id', 21864], ['id', 40029], ['id', 14725], ['id', 9033], ['id', 59215], ['id', 29354], ['id', 23980], ['id', 34753]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4108119010925293, 0.41002070903778076, 0.39407920837402344, 0.3762890100479126, 0.373370885848999, 0.3722800016403198, 0.36701542139053345, 0.3658566474914551, 0.36124300956726074, 0.355975866317749]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.4895429611206055})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.3337615728378296})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2618392705917358})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2497999668121338})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.294920802116394})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.493666172027588})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.445288896560669})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6624, 'crossentropy': 1.2503958984375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.2811675071716309})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1230268478393555})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1008291244506836})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.051114797592163})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.046974539756775})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0818815231323242})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 3437], ['id', 41355], ['id', 23945], ['id', 50770], ['id', 29450], ['id', 36451], ['id', 10760], ['id', 18255], ['id', 49127], ['id', 18676]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5043494701385498, 0.49946755170822144, 0.47619086503982544, 0.4548206925392151, 0.45070314407348633, 0.44136643409729004, 0.4308706521987915, 0.4281769394874573, 0.4265490174293518, 0.42340928316116333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.4814453125, 'crossentropy': 1.4755792617797852})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.2128437757492065})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1296908855438232})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1753904819488525})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2415616512298584})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2607015371322632})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6479, 'crossentropy': 1.16530341796875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.1985574960708618})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.157402753829956})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1318787336349487})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.0731120109558105})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.0833015441894531})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 22946], ['id', 51152], ['id', 54078], ['id', 28356], ['id', 23051], ['id', 24084], ['id', 32171], ['id', 47513], ['id', 33232], ['id', 50381]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36825430393218994, 0.3680340051651001, 0.36213409900665283, 0.36196768283843994, 0.3563617467880249, 0.3516206741333008, 0.3492077589035034, 0.3459930419921875, 0.3445936441421509, 0.3440605401992798]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.4228515625, 'crossentropy': 1.5547993183135986})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3251891136169434})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1239937543869019})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1933503150939941})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1491899490356445})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1367847919464111})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6327, 'crossentropy': 1.1446095703125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.4161123037338257})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.2456798553466797})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.1718096733093262})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.1891971826553345})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1704638004302979})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 27672], ['ood', 2410], ['ood', 2073], ['id', 59671], ['ood', 29434], ['id', 50846], ['ood', 19999], ['ood', 55625], ['ood', 30594], ['ood', 29640]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4094083309173584, 0.39877521991729736, 0.3982890844345093, 0.3862191438674927, 0.38426339626312256, 0.3832716941833496, 0.38155579566955566, 0.3761948347091675, 0.37071919441223145, 0.36943256855010986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.515625, 'crossentropy': 1.4308098554611206})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1989935636520386})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.066908597946167})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1346005201339722})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0149403810501099})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.046384572982788})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2013781070709229})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.2036759853363037})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6985, 'crossentropy': 1.0777775390625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1979732513427734})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0263707637786865})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 0.9678786396980286})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 0.9569279551506042})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9078149795532227})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9046891331672668})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 0.9150558114051819})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 45096], ['id', 23505], ['id', 23401], ['id', 5346], ['ood', 29255], ['ood', 24475], ['ood', 56964], ['id', 11374], ['id', 27719], ['ood', 39313]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.610793948173523, 0.5461287498474121, 0.5458875298500061, 0.5133552551269531, 0.5106959342956543, 0.49875199794769287, 0.485698938369751, 0.48421311378479004, 0.48083066940307617, 0.48061931133270264]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 1.4520142078399658})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.210552453994751})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1019394397735596})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0717096328735352})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1251239776611328})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2742223739624023})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1384179592132568})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6767, 'crossentropy': 1.08649658203125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2544419765472412})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1200363636016846})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0466409921646118})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 0.995765209197998})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 0.9948664903640747})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0126770734786987})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 19174], ['id', 28543], ['id', 34655], ['id', 27477], ['id', 55906], ['id', 13883], ['id', 43542], ['id', 43876], ['id', 16154], ['id', 8921]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4544031620025635, 0.40300190448760986, 0.4028186798095703, 0.3999302387237549, 0.3941583037376404, 0.3939354419708252, 0.3928077220916748, 0.3921070098876953, 0.3913494944572449, 0.3864610195159912]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.5492541790008545})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.2866430282592773})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0761268138885498})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0329017639160156})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0992918014526367})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.110921859741211})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1048598289489746})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.681, 'crossentropy': 1.05566337890625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.3213322162628174})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1216109991073608})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.0814366340637207})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0395911931991577})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.0793836116790771})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0426220893859863})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 1275], ['id', 45510], ['ood', 32393], ['id', 47927], ['id', 13995], ['id', 45908], ['id', 1325], ['id', 3694], ['id', 28962], ['id', 20471]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4356651306152344, 0.4008747339248657, 0.36041009426116943, 0.35000181198120117, 0.3435631990432739, 0.3427119255065918, 0.3408536911010742, 0.34070420265197754, 0.3351384401321411, 0.33494406938552856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.51171875, 'crossentropy': 1.4591197967529297})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2281584739685059})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.1555285453796387})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.072239637374878})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1199278831481934})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.229169249534607})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1947667598724365})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6717, 'crossentropy': 1.0834150390625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3602752685546875})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1566826105117798})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.0790612697601318})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0438625812530518})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0284717082977295})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.031768560409546})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 35384], ['id', 47206], ['id', 41666], ['id', 18584], ['id', 54123], ['id', 28099], ['id', 50582], ['id', 19291], ['id', 243], ['id', 15124]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41392672061920166, 0.4068070650100708, 0.39215266704559326, 0.39058375358581543, 0.38785815238952637, 0.3835815191268921, 0.3833571672439575, 0.3791149854660034, 0.37771880626678467, 0.3773200511932373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.52734375, 'crossentropy': 1.5394970178604126})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2590935230255127})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1626152992248535})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1238045692443848})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1105294227600098})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.125462293624878})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2233154773712158})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1662933826446533})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6673, 'crossentropy': 1.12458701171875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3040745258331299})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1299784183502197})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0575402975082397})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0763769149780273})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0486702919006348})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.026993989944458})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.042358636856079})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 29187], ['id', 1342], ['id', 24005], ['id', 35163], ['id', 20348], ['id', 12426], ['id', 5442], ['id', 59953], ['id', 38917], ['id', 38551]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4612997770309448, 0.4284600019454956, 0.37867307662963867, 0.37581145763397217, 0.371451735496521, 0.3639993667602539, 0.3634207248687744, 0.36280661821365356, 0.35914868116378784, 0.35799258947372437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.4951171875, 'crossentropy': 1.5234274864196777})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.3069846630096436})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1078424453735352})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0807266235351562})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0988502502441406})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1662516593933105})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.09678316116333})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6709, 'crossentropy': 1.1123216796875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2271932363510132})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.094435453414917})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.0767093896865845})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.059526801109314})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.04069185256958})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0119669437408447})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 56635], ['id', 35305], ['id', 58320], ['id', 31065], ['ood', 52838], ['id', 41229], ['id', 53741], ['id', 13257], ['id', 37709], ['id', 40979]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39703989028930664, 0.3496837615966797, 0.3496081829071045, 0.34930145740509033, 0.34453678131103516, 0.33992332220077515, 0.3375128507614136, 0.3374321460723877, 0.3354238271713257, 0.3326359987258911]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.527073621749878})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2349231243133545})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1581449508666992})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0898044109344482})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1038572788238525})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0797533988952637})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1201245784759521})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2342822551727295})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2041890621185303})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6804, 'crossentropy': 1.09116494140625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.3301019668579102})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.1166489124298096})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.0345468521118164})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.0194529294967651})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0203317403793335})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 0.9928246736526489})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 0.9966777563095093})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 0.9716466069221497})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 52833], ['id', 39951], ['id', 2096], ['id', 51188], ['ood', 59468], ['id', 1799], ['id', 6155], ['id', 42976], ['id', 31216], ['id', 12645]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.44176244735717773, 0.41588449478149414, 0.406109094619751, 0.40084362030029297, 0.3954848051071167, 0.3948477506637573, 0.39364683628082275, 0.3879772424697876, 0.38635504245758057, 0.38536369800567627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.5011537075042725})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.1705710887908936})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0385267734527588})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0570029020309448})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.049084186553955})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9866729378700256})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0915013551712036})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0826750993728638})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.1131503582000732})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6983, 'crossentropy': 1.00283212890625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2685075998306274})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0328339338302612})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 0.948926568031311})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 0.9623594880104065})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 0.9548131227493286})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 0.9246689081192017})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.8888751268386841})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9045212268829346})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 45484], ['id', 59105], ['id', 16797], ['id', 41759], ['id', 16443], ['id', 17030], ['id', 21478], ['id', 48671], ['id', 30644], ['id', 31048]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4614614248275757, 0.4521220326423645, 0.4343351125717163, 0.42867565155029297, 0.4139167070388794, 0.41131365299224854, 0.40763598680496216, 0.4070761799812317, 0.40611088275909424, 0.3960484266281128]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.458984375, 'crossentropy': 1.5696403980255127})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2491645812988281})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0902869701385498})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0666476488113403})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0576026439666748})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0662480592727661})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0934269428253174})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.026484489440918})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1890758275985718})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2291669845581055})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2093968391418457})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6909, 'crossentropy': 1.0832986328125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2469146251678467})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0501809120178223})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.013383388519287})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.9563902616500854})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.9662140607833862})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9642420411109924})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 0.9263132810592651})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.9297340512275696})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.9001685976982117})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9050158858299255})
store['active_learning_steps'][36]['eval_training']['best_epoch']=9
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 4436], ['id', 36], ['id', 53447], ['id', 53488], ['id', 49763], ['id', 40210], ['id', 42265], ['id', 36592], ['id', 13068], ['id', 52961]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4668900966644287, 0.45553797483444214, 0.4391636848449707, 0.43807393312454224, 0.43474048376083374, 0.43040305376052856, 0.41829216480255127, 0.4152263402938843, 0.4141042232513428, 0.41214656829833984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.465662956237793})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1463310718536377})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1240768432617188})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.053659200668335})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0436822175979614})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9837790131568909})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0508867502212524})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.098097801208496})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.138897180557251})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.7068, 'crossentropy': 1.0025474609375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2311432361602783})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0243299007415771})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9994450807571411})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9605580568313599})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9476022720336914})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9592056274414062})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9092446565628052})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9145696759223938})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 54667], ['id', 28398], ['id', 1582], ['id', 27297], ['id', 49125], ['id', 28835], ['id', 36659], ['ood', 16204], ['id', 20657], ['id', 37658]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.45017576217651367, 0.4386689066886902, 0.4300687909126282, 0.42824786901474, 0.42624497413635254, 0.42342543601989746, 0.4232531189918518, 0.4201887845993042, 0.4179982542991638, 0.4168205261230469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.4598534107208252})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.17971932888031})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0484423637390137})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0037076473236084})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0807957649230957})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0692156553268433})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0562511682510376})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6784, 'crossentropy': 1.0375775390625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2533016204833984})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1065605878829956})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.050210952758789})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0251905918121338})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.011945366859436})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0348658561706543})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 19888], ['id', 19136], ['id', 53796], ['id', 31705], ['id', 15877], ['id', 42950], ['id', 34579], ['id', 16803], ['id', 39615], ['id', 19587]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3337521553039551, 0.309711217880249, 0.30271703004837036, 0.3019062876701355, 0.30177879333496094, 0.2927539348602295, 0.2918318510055542, 0.2854214906692505, 0.2835958003997803, 0.27938127517700195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.494140625, 'crossentropy': 1.4837801456451416})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2031781673431396})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0872530937194824})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0757091045379639})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0252363681793213})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.052248477935791})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.088405966758728})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0461204051971436})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6782, 'crossentropy': 1.02426279296875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.231428623199463})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0876259803771973})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 0.9967111349105835})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 0.964537501335144})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 0.9674136638641357})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.950688898563385})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9471146464347839})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 58220], ['id', 26636], ['id', 28173], ['id', 2731], ['id', 9302], ['ood', 10259], ['id', 46903], ['id', 801], ['id', 39553], ['id', 17738]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.37660467624664307, 0.3687902092933655, 0.36367368698120117, 0.3613142967224121, 0.35441553592681885, 0.34543800354003906, 0.3406243920326233, 0.3395366668701172, 0.3325529098510742, 0.33182621002197266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.4883018732070923})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.2246229648590088})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.093000054359436})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.113755226135254})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0776607990264893})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.150331974029541})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1464424133300781})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1369643211364746})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6727, 'crossentropy': 1.08059306640625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.3136134147644043})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1022660732269287})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.0664069652557373})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0803804397583008})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.006704330444336})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0340869426727295})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0528323650360107})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 37713], ['id', 47659], ['id', 33141], ['id', 7593], ['id', 29501], ['id', 41019], ['id', 6000], ['id', 1254], ['id', 25706], ['id', 46197]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4034740626811981, 0.36517059803009033, 0.36448633670806885, 0.35819727182388306, 0.342349648475647, 0.341904878616333, 0.3214116096496582, 0.3164123296737671, 0.31034600734710693, 0.30654042959213257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.4078118801116943})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.221120834350586})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.087247610092163})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0826786756515503})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0742518901824951})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0252127647399902})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1190557479858398})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0789985656738281})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2443102598190308})
store['active_learning_steps'][41]['training']['best_epoch']=6
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6958, 'crossentropy': 1.0596671875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2830369472503662})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.092665672302246})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.031578540802002})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 0.9933959245681763})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 0.9804141521453857})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 0.9833723306655884})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0049269199371338})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 0.9757907390594482})
store['active_learning_steps'][41]['eval_training']['best_epoch']=8
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 43215], ['id', 48278], ['id', 6049], ['id', 57817], ['id', 34817], ['id', 33311], ['id', 43859], ['id', 2273], ['id', 47494], ['id', 11956]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.42127466201782227, 0.41687774658203125, 0.4132435917854309, 0.3898879289627075, 0.3885312080383301, 0.3703157901763916, 0.36794114112854004, 0.36491239070892334, 0.36145734786987305, 0.3610187768936157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.4853515625, 'crossentropy': 1.4613720178604126})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2146406173706055})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1191835403442383})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0972425937652588})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0526068210601807})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0716698169708252})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1107553243637085})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1903191804885864})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6722, 'crossentropy': 1.044093359375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.3025439977645874})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.101626992225647})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0626736879348755})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0032761096954346})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.0407347679138184})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0037269592285156})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 0.9978867173194885})
store['active_learning_steps'][42]['eval_training']['best_epoch']=7
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 8455], ['id', 50403], ['id', 44285], ['id', 8900], ['id', 21282], ['id', 47410], ['id', 3878], ['id', 23586], ['id', 995], ['id', 18670]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.35368967056274414, 0.3477221727371216, 0.33923888206481934, 0.33735454082489014, 0.3328530788421631, 0.3237757682800293, 0.32226109504699707, 0.3217822313308716, 0.32164978981018066, 0.3198208808898926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.5187206268310547})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.229278326034546})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1028883457183838})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0312259197235107})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.074976921081543})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0538926124572754})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.05631685256958})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6787, 'crossentropy': 1.04712724609375}
